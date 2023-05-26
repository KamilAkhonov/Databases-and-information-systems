# Report | Отчет

1. Сгенерировать большие (>100000 записей) таблицы со случайными данными – числами и строками (с помощью хранимой процедуры)
2. Создать индексы (на отдельные поля и составные)
3. Сравнить время заполнения таблиц с индексами и без них.
4. Сравнить время выполнения запросов (с условием отбора и с сортировкой) с индексами и без них.
5. Модифицировать таблицу в своей БД, добавив партицирование.
6. Продемонстрировать, что это не «ломает» запросов.

Сгенерировать большие (>100000 записей) таблицы со случайными данными – числами и строками (с помощью хранимой процедуры)
```Mysql
CREATE DEFINER=`root`@`localhost` PROCEDURE `generate_lessons`(IN count INT)
BEGIN
	DECLARE i INT DEFAULT 0;
	DECLARE days_of_week VARCHAR(255);
	DECLARE start_time TIME;
	DECLARE end_time TIME;
	DECLARE classroom_id INT;
	DECLARE group_id INT;
	DECLARE discipline_id INT;
	DECLARE teacher_id INT;

	SET days_of_week = 'Понедельник,Вторник,Среда,Четверг,Пятница,Суббота,Воскресенье';

	WHILE i < count DO
	SET start_time = SEC_TO_TIME(RAND() * 86400);
	SET end_time = ADDTIME(start_time,SEC_TO_TIME(RAND() * 7200));
	SET classroom_id = FLOOR(RAND() * 15) + 1;
	SET group_id = FLOOR(RAND() * 5) + 1;
	SET discipline_id = FLOOR(RAND() * 10) + 1;
	SET teacher_id = FLOOR(RAND() * 10) + 1;

	INSERT INTO lessons (DayOfWeek, StartTime, EndTime, ClassroomID, GroupID, DisciplineID, TeacherID) VALUES (SUBSTRING_INDEX(SUBSTRING_INDEX(days_of_week, ',', FLOOR(RAND() * 7) + 1), ',', -1), start_time, end_time, classroom_id, group_id, discipline_id, teacher_id);

	SET i = i + 1;
END WHILE;
END
```
Создать индексы на (отдельные поля и составные)
```Mysql
CREATE INDEX idx_lessons_ClassroomID_ID ON lessons (ClassroomID, ID);
CREATE INDEX idx_lessons_ClassroomID ON lessons (ClassroomID);
```

## Результаты эксперимента

Были созданы таблицы со случайными данными с помощью хранимой процедуры `generate_lessons`. Были созданы индексы на поля `ClassroomID` и `ID`, а также на поле `ClassroomID`. Были измерены времена заполнения таблиц без индексов, со сингл-индексом и с составным индексом.

| Колонка 1 | Колонка 2 | Колонка 3 | Колонка 4 | Колонка 5 | Колонка 6 |
| --- | --- | --- | --- | --- | --- |
| 3 | 70 | 19:46:49 | CALL generate_lessons(5000) | 1 row(s) affected | 16.750 sec |
| 3 | 67 | 19:45:50 | CALL generate_lessons(5000) | 1 row(s) affected | 16.781 sec |
| 3 | 64 | 19:44:57 | CALL generate_lessons(5000) | 1 row(s) affected | 16.672 sec |

Как видно из таблицы, заполнение таблиц без индексов происходит быстрее, чем с индексами.

Также были измерены времена выполнения запросов с условием отбора и с сортировкой, как с индексами, так и без них. Результаты измерений представлены в таблице ниже.

| Колонка 1 | Колонка 2 | Колонка 3 | Колонка 4 | Колонка 5 | Колонка 6 |
| --- | --- | --- | --- | --- | --- |
| 3 | 98 | 22:30:25 | select * from lessons_test FORCE INDEX (idx_lessons_test_GroupID_ClassroomID) where (ClassroomID between 5 and 10) AND (GroupID = 5) | 27859 row(s) returned | 0.000 sec / 0.109 sec |
| 3 | 99 | 22:30:25 | select * from lessons_test2 FORCE INDEX (idx_lessons_test2_ClassroomID) where (ClassroomID between 5 and 10) AND (GroupID = 5) | 28004 row(s) returned | 0.000 sec / 0.437 sec |
| 3 | 100 | 22:30:26 | select * from lessons_test3 where (ClassroomID between 5 and 10) AND (GroupID = 5) | 28032 row(s) returned | 0.000 sec / 0.187 sec |
| 3 | 86 | 22:27:34 | select * from lessons_test FORCE INDEX (idx_lessons_test_GroupID_ClassroomID) ORDER BY GroupID,ClassroomID | 350000 row(s) returned | 0.000 sec / 1.125 sec |
| 3 | 87 | 22:27:36 | select * from lessons_test2 ORDER BY GroupID,ClassroomID | 350000 row(s) returned | 0.640 sec / 0.235 sec |
| 3 | 88 | 22:27:39 | select * from lessons_test3 ORDER BY GroupID,ClassroomID | 350000 row(s) returned | 0.672 sec / 0.297 sec |
| 3 | 102 | 22:31:56 | select * from lessons_test FORCE INDEX (idx_lessons_test_GroupID_ClassroomID) where (ClassroomID between 5 and 10) AND (GroupID = 5) ORDER BY GroupID,ClassroomID | 27859 row(s) returned | 0.000 sec / 0.110 sec |


| 3 | 103 | 22:31:57 | select * from lessons_test2 FORCE INDEX (idx_lessons_test2_ClassroomID) where (ClassroomID between 5 and 10) AND (GroupID = 5) ORDER BY GroupID,ClassroomID | 28004 row(s) returned | 0.000 sec / 0.438 sec |
| 3 | 104 | 22:31:57 | select * from lessons_test3 where (ClassroomID between 5 and 10) AND (GroupID = 5) ORDER BY GroupID,ClassroomID | 28032 row(s) returned | 0.204 sec / 0.015 sec |

Из таблицы видно, что использование индексов позволяет выбирать данные быстрее, сортировать запросы также можно быстрее при использования индексов. Но для таблиц со случайными данными размером >100000 записей использование индексов не дает существенной выгоды при заполнении таблиц, их преимущества проявляются при выполнении запросов. Составные индексы работают еще более эффективно, чем сингл-индексы.

```
Модифицировать таблицу в своей БД, добавив партицирование.

```sql
CREATE TABLE lessons_partitioned (
    ID INT NOT NULL,
    DayOfWeek VARCHAR(10),
    StartTime TIME,
    EndTime TIME,
    ClassroomID INT,
    GroupID INT,
    DisciplineID INT,
    TeacherID INT
)
PARTITION BY LIST (GroupID)
(
    PARTITION p1 VALUES IN (1),
    PARTITION p2 VALUES IN (2),
    PARTITION p3 VALUES IN (3),
    PARTITION p4 VALUES IN (4),
    PARTITION p5 VALUES IN (5)
);
```
Продемонстрировать, что это не «ломает» запросов.

```sql
SELECT * FROM lessons_partitioned partition(p1) where ClassroomID = 10;
```

В результате запроса будут получены 20 строк, что говорит о том, что добавление партиций не повлияло на работу запросов к таблице.
