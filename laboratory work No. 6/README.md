# Отчет | Report

1. Создать 2-х пользователей и 2 роли
2. Наделить их разными полномочиями на уровне таблиц/столбцов и процедур. Продемонстрировать запросами. 

```Mysql
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'password1';
CREATE USER 'user2'@'localhost' IDENTIFIED BY 'password2';
CREATE ROLE 'role1';
CREATE ROLE 'role2';
GRANT SELECT, INSERT ON shedule.disciplines TO 'user1'@'localhost';
GRANT SELECT, UPDATE(StartTime, EndTime) ON shedule.lessons TO 'user1'@'localhost';
GRANT EXECUTE ON PROCEDURE shedule.show_schedule TO 'user1'@'localhost';
```

Запросы

```Mysql
SELECT * FROM disciplines;
UPDATE lessons SET GroupID = 500; 
CALL show_schedule('Ежики');
```

Результаты:

![image](https://github.com/Lszoa/Databases-and-information-systems/assets/115508876/986f0fb3-9c48-42cd-94c9-9041e4b3e19f)

```Mysql
GRANT SELECT, UPDATE ON shedule.teachers TO 'user2'@'localhost';
GRANT SELECT, INSERT(TeacherID) ON shedule.lessons TO 'user2'@'localhost';
GRANT EXECUTE ON PROCEDURE shedule.delete_teacher_lessons TO 'user2'@'localhost';
```

```Mysql
SELECT * FROM disciplines;
INSERT INTO lessons(TeacherID) VALUES (6); 
CALL show_schedule()
```

Результаты:

![image](https://github.com/Lszoa/Databases-and-information-systems/assets/115508876/31021e4d-10f2-4b3c-a920-87cae35aa5f0)

```Mysql
GRANT 'role1' TO 'user1'@'localhost';  
GRANT 'role2' TO 'user2'@'localhost';
```
