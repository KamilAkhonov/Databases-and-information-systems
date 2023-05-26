# Report | Отчет
Задание 1: Для своего варианта задания сделать представление (с ограничением по строкам и столбцам)
Задание 2: Для своего варианта задания сделать хранимую процедуру, использующую курсор.

-----

Представление с ограничением по столбцам и строкам
```Mysql
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `weekly_teacher_disciplines` AS
    SELECT 
        `t`.`Fullname` AS `FullName`,
        COUNT(DISTINCT `l`.`DisciplineID`) AS `NumDisciplines`
    FROM
        (`lessons` `l`
        JOIN `teachers` `t` ON ((`t`.`ID` = `l`.`TeacherID`)))
    GROUP BY `t`.`ID`
    ORDER BY `NumDisciplines` DESC
    LIMIT 3
```

Хранимая процедура, использующая курсор
```Mysql
CREATE DEFINER=`root`@`localhost` PROCEDURE `show_schedule`(IN group_name VARCHAR(255))
BEGIN
    DECLARE lesson_id INT;
    DECLARE lesson_day VARCHAR(20);
    DECLARE lesson_start_time TIME;
    DECLARE lesson_end_time TIME;
    DECLARE classroom_id INT;
    DECLARE discipline_name VARCHAR(255);
    DECLARE teacher_name VARCHAR(255);
    
    DECLARE lesson_cursor CURSOR FOR
        SELECT lessons.ID, lessons.DayOfWeek, lessons.StartTime, lessons.EndTime, 
               lessons.ClassroomID, disciplines.DisciplineName, teachers.FullName
        FROM lessons
        INNER JOIN disciplines ON lessons.DisciplineID = disciplines.ID
        INNER JOIN teachers ON lessons.TeacherID = teachers.ID
        WHERE lessons.GroupID = (SELECT ID FROM groupstud WHERE GroupName = group_name);

    OPEN lesson_cursor;

    lesson_loop: LOOP
        FETCH lesson_cursor INTO lesson_id, lesson_day, lesson_start_time, lesson_end_time, classroom_id, discipline_name, teacher_name;
        IF (lesson_id IS NULL) THEN
            LEAVE lesson_loop;
        END IF;
        SELECT lesson_id, lesson_day, lesson_start_time, lesson_end_time, classroom_id, discipline_name, teacher_name;
    END LOOP;

    CLOSE lesson_cursor;
END
```
