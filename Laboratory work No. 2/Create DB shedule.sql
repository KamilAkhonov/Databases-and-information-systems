USE shedule;

-- Подсчет пар в неделю у конкретного преподавателя
-- SELECT count_lessons_by_teacher(2);
-- Поиск самого загруженного дня для группы
-- SELECT max_lessons_day_by_group('Тигры');
-- Выборка предметов, которые изучает указанная группа
-- CALL get_disciplines_by_group('Ежики');
-- Удаление преподавателя из расписания
-- CALL delete_teacher_lessons('Новикова О.П.');
-- Триггер на добавление неправильного времени окончания занятия
-- INSERT INTO lessons (DayOfWeek, StartTime, EndTime, ClassroomID, GroupID, DisciplineID, TeacherID) VALUES
-- ('Понедельник', '08:00:00', '07:30:00', 1, 1, 1, 1);
-- Удаление группы вызывает триггер на удаление пар и студентов этой группы 
-- DELETE FROM groupstud WHERE ID = 4;

-- CALL generate_lessons(200000);
-- select * from lessons_test where (ClassroomID between 5 and 10) AND (GroupID = 5);
-- select * from lessons_test2 where (ClassroomID between 5 and 10) AND (GroupID = 5);
-- select * from lessons_test3 where (ClassroomID between 5 and 10) AND (GroupID = 5);

-- select * from lessons_test FORCE INDEX (idx_lessons_test_GroupID_ClassroomID) where (ClassroomID between 5 and 10) AND (GroupID = 5) ORDER BY GroupID,ClassroomID;
-- select * from lessons_test2 FORCE INDEX (idx_lessons_test2_ClassroomID) where (ClassroomID between 5 and 10) AND (GroupID = 5) ORDER BY GroupID,ClassroomID;
-- select * from lessons_test3 where (ClassroomID between 5 and 10) AND (GroupID = 5) ORDER BY GroupID,ClassroomID;

-- CALL generate_lessons(1000);

SELECT * FROM lessons_partitioned partition(p1) where ClassroomID = 10;




