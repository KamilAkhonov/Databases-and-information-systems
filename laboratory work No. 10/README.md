# Отчет | Report

1. Выполнить запрос на выборку с объединением
2. Выполнить запрос с использованием рекурсивного CTE
3. Выполнить запрос с использованием оконной функции

Выполнить запрос на выборку с объединением.
Получение списка всех учителей и всех студентов:
```Mysql
SELECT teachers.ID, FullName, NULL AS GroupName FROM teachers
UNION
SELECT students.ID, FullName, GroupName FROM students
JOIN groupstud ON students.GroupID = groupstud.ID;
```
![image](https://github.com/Lszoa/Databases-and-information-systems/assets/115508876/25af7354-72f8-4e24-bc3c-db463e5011c9)

Выполнить запрос с использованием оконной функции
Выбрать список студентов, отсортированный по фамилии и имени, и указать номер строки (порядковый номер студента в списке):
```Mysql
SELECT ROW_NUMBER() OVER (ORDER BY Fullname) AS RowNum, Fullname, GroupID
FROM students
ORDER BY Fullname;
```
![image](https://github.com/Lszoa/Databases-and-information-systems/assets/115508876/58072806-35ac-45c7-aa59-a48fc123feea)

Выполнить запрос с использованием рекурсивного CTE:
Создадим таблицу с иерархической структурой:
![image](https://github.com/Lszoa/Databases-and-information-systems/assets/115508876/917050c9-488b-48e3-b642-54e52ae861c0)

Рекурсивный запрос, выполняющий выгрузку факультетов Технического института:
```Mysql
WITH RECURSIVE Institutes AS (
  SELECT ID, Name, InstituteID
  FROM faculty
  WHERE ID = 1 AND InstituteID IS NULL
  UNION ALL
  SELECT f.ID, f.Name, f.InstituteID
  FROM faculty f
  JOIN Institutes i ON f.InstituteID = i.ID
)
SELECT *
FROM Institutes;
```
![image](https://github.com/Lszoa/Databases-and-information-systems/assets/115508876/46b8c903-839e-45e1-9a0a-f9a80e9972f2)

Если ID = 2:
![image](https://github.com/Lszoa/Databases-and-information-systems/assets/115508876/758eebd4-3061-4c45-99f1-dc3bf81ff38a)
