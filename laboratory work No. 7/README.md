# Report | Отчет

1. Установить отладчик и продемонстрировать выполнение процедуры по шагам
2. Сгенерировать большие (>100000 записей) таблицы со случайными данными – числами и строками (с помощью хранимой процедуры)
3. Создать индексы (на отдельные поля и составные)
4. Сравнить время заполнения таблиц с индексами и без них.
5. Сравнить время выполнения запросов (с условием отбора и с сортировкой) с индексами и без них.
6. Модифицировать таблицу в своей БД, добавив партицирование.
7. Продемонстрировать, что это не «ломает» запросов.

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
Сравнить время заполнения таблиц с индексами и без них

Таблица с индексом на поля ClassroomID и ID:

| 3 | 70 | 19:46:49 | CALL generate_lessons(5000) | 1 row(s) affected | 16.750 sec |

Таблица с индексом на поле ClassroomID:

| 3	| 67	| 19:45:50	| CALL generate_lessons(5000)	| 1 row(s) | affected	| 16.781 sec |

Таблица без индекса:

| 3	| 64	| 19:44:57	| CALL generate_lessons(5000)	| 1 row(s) | affected	| 16.672 sec |

**Вывод: таблица без индексов заполняется быстрее**

Сравнить время выполнения запросов (с условием отбора и с сортировкой) с индексами и без них.
С условием отбора:
|3	|98|	22:30:25|	```Mysql select * from lessons_test FORCE INDEX (idx_lessons_test_GroupID_ClassroomID) where (ClassroomID between 5 and 10) AND (GroupID = 5)```|	27859 row(s) returned	| 0.000 sec / 0.109 sec |
|3|	99|	22:30:25|	```Mysql select * from lessons_test2 FORCE INDEX (idx_lessons_test2_ClassroomID) where (ClassroomID between 5 and 10) AND (GroupID = 5)```	|28004 row(s) returned	| 0.000 sec / 0.437 sec|
| 3 |	100	| 22:30:26	| ```Mysql select * from lessons_test3 where (ClassroomID between 5 and 10) AND (GroupID = 5)```	|28032 row(s) returned|	0.000 sec / 0.187 sec|
