Скрипты создания таблиц:

```MYSQL
-- Таблица "Студенты"
CREATE TABLE Students (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  GroupID INT,
  Fullname VARCHAR(255),
  FOREIGN KEY (GroupID) REFERENCES Groupstud(ID)
);
```
8. 
9.-- Таблица "Группы"
10.CREATE TABLE Groupstud (
11.  ID INT PRIMARY KEY AUTO_INCREMENT,
12.  GroupName VARCHAR(255)
13.);
14. 
15.-- Таблица "Дисциплины"
16.CREATE TABLE Disciplines (
17.  ID INT PRIMARY KEY AUTO_INCREMENT,
18.  DisciplineName VARCHAR(255)
19.);
20. 
21.-- Таблица "Аудитории"
22.CREATE TABLE Classrooms (
23.  ID INT PRIMARY KEY AUTO_INCREMENT,
24.  ClassroomNumber VARCHAR(255),
25.  Building VARCHAR(255)
26.);
27. 
28.-- Таблица "Преподаватели"
29.CREATE TABLE Teachers (
30.  ID INT PRIMARY KEY AUTO_INCREMENT,
31.  Fullname VARCHAR(255)
32.);
33. 
34.-- Таблица "Пары"
35.CREATE TABLE Lessons (
36.  ID INT PRIMARY KEY AUTO_INCREMENT,
37.  DayOfWeek VARCHAR(255),
38.  StartTime TIME,
39.  EndTime TIME,
40.  ClassroomID INT,
41.  GroupID INT,
42.  DisciplineID INT,
43.  TeacherID INT,
44.  FOREIGN KEY (ClassroomID) REFERENCES Classrooms(ID),
45.  FOREIGN KEY (GroupID) REFERENCES Groupstud(ID),
46.  FOREIGN KEY (DisciplineID) REFERENCES Disciplines(ID),
47.  FOREIGN KEY (TeacherID) REFERENCES Teachers(ID)
48.);
Добавление преподавателей
1.INSERT INTO teachers (Fullname) VALUES
2.('Иванов В.В.'),
3.('Петров А.И.'),
4.('Сидорова Е.А.'),
5.('Козлов И.Н.'),
6.('Новикова О.П.'),
7.('Лебедев Д.В.'),
8.('Калинина Н.Н.'),
9.('Смирнова Е.А.'),
10.('Тимофеев Д.А.'),
11.('Антонова Е.А.');
Добавление групп
1.INSERT INTO groupstud (GroupName) values
2.('Ежики'),
3.('Тигры'),
4.('Кролики'),
5.('Носороги'),
6.('Зебры');
Добавление дисциплин
1.INSERT INTO disciplines (DisciplineName) VALUES
2.('Математика'),
3.('Физика'),
4.('Компьютерные науки'),
5.('Инженерная механика'),
6.('Электротехника'),
7.('Материаловедение'),
8.('Технология производства'),
9.('Химия'),
10.('Геодезия и картография'disciplines),
11.('Архитектура и дизайн');
Добавление Аудиторий
1.INSERT INTO classrooms (ClassroomNumber, Building) VALUES
2.('A10','A'),
3.('A11','A'),
4.('A12','A'),
5.('A13','A'),
6.('A14','A'),
7.('B10','B'),
8.('B11','B'),
9.('B12','B'),
10.('B13','B'),
11.('B14','B'),
12.('C10','C'),
13.('C11','C'),
14.('C12','C'),
15.('C13','C'),
16.('C14','C');
Добавляем студентов
1.INSERT INTO students (GroupID, Fullname) VALUES
2.(1, 'Студент 1'),
3.(1, 'Студент 2'),
4.(1, 'Студент 3'),
5.(1, 'Студент 4'),
6.(1, 'Студент 5'),
7.(2, 'Студент 1'),
8.(2, 'Студент 2'),
9.(2, 'Студент 3'),
10.(2, 'Студент 4'),
11.(2, 'Студент 5'),
12.(3, 'Студент 1'),
13.(3, 'Студент 2'),
14.(3, 'Студент 3'),
15.(3, 'Студент 4'),
16.(3, 'Студент 5'),
17.(4, 'Студент 1'),
18.(4, 'Студент 2'),
19.(4, 'Студент 3'),
20.(5, 'Студент 1'),
21.(5, 'Студент 2'),
22.(5, 'Студент 3'),
23.(5, 'Студент 4');
Заполнение расписания
1.INSERT INTO lessons (DayOfWeek, StartTime, EndTime, ClassroomID, GroupID, DisciplineID, TeacherID) VALUES
2.('Понидельник', '08:00:00', '09:30:00', 1, 1, 1, 1),
3.('Понидельник', '10:00:00', '11:30:00', 1, 2, 1, 1),
4.('Понидельник', '08:00:00', '09:30:00', 2, 3, 1, 2),
5.('Понидельник', '11:30:00', '13:00:00', 3, 1, 2, 2),
6.('Понидельник', '08:00:00', '09:30:00', 4, 4, 6, 5),
7. 
8.('Вторник', '08:00:00', '09:30:00', 1, 1, 1, 2),
9.('Вторник', '10:00:00', '11:30:00', 1, 2, 1, 3),
10.('Вторник', '08:00:00', '09:30:00', 2, 3, 1, 4),
11.('Вторник', '11:30:00', '13:00:00', 3, 1, 2, 5),
12.('Вторник', '08:00:00', '09:30:00', 4, 4, 6, 6),
13. 
14.('Среда', '08:00:00', '09:30:00', 1, 1, 2, 1),
15.('Среда', '10:00:00', '11:30:00', 1, 2, 2, 1),
16.('Среда', '08:00:00', '09:30:00', 2, 3, 2, 2),
17.('Среда', '11:30:00', '13:00:00', 3, 1, 3, 2),
18.('Среда', '08:00:00', '09:30:00', 4, 4, 7, 5),
19. 
20.('Четверг', '08:00:00', '09:30:00', 2, 1, 2, 1),
21.('Четверг', '10:00:00', '11:30:00', 2, 2, 2, 1),
22.('Четверг', '08:00:00', '09:30:00', 3, 3, 2, 2),
23.('Четверг', '11:30:00', '13:00:00', 4, 1, 3, 2),
24.('Четверг', '08:00:00', '09:30:00', 5, 4, 7, 5),
25. 
26.('Пятница', '08:00:00', '09:30:00', 2, 2, 2, 1),
27.('Пятница', '10:00:00', '11:30:00', 2, 3, 2, 1),
28.('Пятница', '08:00:00', '09:30:00', 3, 4, 2, 2),
29.('Пятница', '11:30:00', '13:00:00', 4, 2, 3, 2),
30.('Пятница', '08:00:00', '09:30:00', 5, 1, 7, 5);
Функция для числовых аргументов
1.CREATE DEFINER=`root`@`localhost` FUNCTION `count_lessons_by_teacher`(teacher_id INT) RETURNS int
2.    READS SQL DATA
3.BEGIN
4.    DECLARE lesson_count INT;
5.    SELECT COUNT(*) INTO lesson_count FROM lessons WHERE TeacherID = teacher_id;
6.    RETURN lesson_count;
7.END
Функция для строковых аргументов
1.CREATE DEFINER=`root`@`localhost` FUNCTION `max_lessons_day_by_group`(group_name VARCHAR(50)) RETURNS varchar(50) CHARSET utf8mb4
2.    READS SQL DATA
3.BEGIN
4.    DECLARE busiest_day VARCHAR(50);
5.    SELECT DayOfWeek
6.    INTO busiest_day
7.    FROM (
8.        SELECT DayOfWeek, COUNT(*) AS count
9.        FROM lessons
10.        JOIN groupstud ON lessons.GroupId = groupstud.ID
11.        WHERE groupstud.GroupName = group_name
12.        GROUP BY DayOfWeek
13.        ORDER BY count DESC
14.        LIMIT 1
15.    ) AS t;
16.    RETURN busiest_day;
17.END
Хранимая процедура для выборки данных
1.CREATE DEFINER=`root`@`localhost` PROCEDURE `get_disciplines_by_group`(IN groupName VARCHAR(50))
2.BEGIN
3.    SELECT DISTINCT d.DisciplineName
4.    FROM lessons l
5.    JOIN disciplines d ON l.DisciplineID = d.ID
6.    JOIN groupstud g ON l.GroupID = g.ID
7.    WHERE g.GroupName = groupName;
8.END
Хранимая процедура для модификации данных
1.CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_teacher_lessons`(
2.    IN p_fullname VARCHAR(255)
3.)
4.BEGIN
5.    DECLARE teacher_id INT;
6. 
7.    SELECT ID INTO teacher_id
8.    FROM teachers
9.    WHERE FullName = p_fullname;
10. 
11.    DELETE FROM lessons
12.    WHERE TeacherID = teacher_id;
13.END
Триггер, запрещающий изменения при определенном условии
1.CREATE DEFINER=`root`@`localhost` TRIGGER `lessons_BEFORE_INSERT` BEFORE INSERT ON `lessons` FOR EACH ROW BEGIN
2.IF NEW.StartTime >= NEW.EndTime THEN
3.        SIGNAL SQLSTATE '45000'
4.        SET MESSAGE_TEXT = 'Start time must be less than end time';
5.    END IF;
6.END
Триггер, модифицирующий изменяющиеся данные
1.CREATE DEFINER=`root`@`localhost` TRIGGER `groupstud_BEFORE_DELETE` BEFORE DELETE ON `groupstud` FOR EACH ROW BEGIN
2.    DELETE FROM students WHERE GroupID = OLD.ID;
3.    DELETE FROM lessons WHERE GroupID = OLD.ID;
4.END
