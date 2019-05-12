USE curriculum_db;

drop table sec_grades;
drop table goal_grades;
drop table course_goals;
drop table curric_reqs;
drop table curric_ops;
drop table topic_curric;
drop table section;
drop table goals;
drop table courses;
drop table topic;
drop table curriculum;





-- Delete old data
DELETE FROM sec_grades;
DELETE FROM goal_grades;
DELETE FROM course_goals;
DELETE FROM curric_reqs;
DELETE FROM curric_ops;
DELETE FROM topic_curric;
DELETE FROM section;
DELETE FROM goals;
DELETE FROM courses;
DELETE FROM topic;
DELETE FROM curriculum;

-- Create Curriculums
INSERT INTO curriculum (curric_name, person_name, person_id, min_hours, min_cover2, min_cover3)
	VALUES ('Computer Science', 'John Doe', '000', 10, 5, 5),
	('Math', 'Jim Beam', '001', 10, 5, 5),
	('English', 'Mr. Bean', '010', 15, 5, 5),
	('Science', 'Simaris', '011', 20, 5, 5);

-- Create Goals
INSERT INTO goals (goal_id, description, curric_name, goal_hrs)
			VALUES (1, 'Computers', 'Computer Science', 5),
			(2, 'Computers2', 'Computer Science', 5),
			(3, 'Maths', 'Math', 5),
			(4, 'Maths2', 'Math', 5), 
			(5, 'Engrish', 'English', 5), 
			(6, 'Engrish2', 'English', 5),
			(7, 'Singlish', 'English', 5),
			(8, 'Space', 'Science', 5), 
			(9, 'Space2', 'Science', 5), 
			(10,'Space3', 'Science', 10);

-- Create Courses
INSERT INTO courses (course_name, subj_code, course_no, cred_hrs, description)
	VALUES ('Computers', '0000', 1, 5, 'Computers'),
	('Writing', '0001', 2, 5, 'English'),
	('Reading', '0001', 3, 5, 'English'),
	('Arithmetic', '0010', 4, 5, 'Math'),
	('Statistics', '0010', 5, 5, 'Math'),
	('Calculus', '0010', 6, 5, 'Math'),
	('Journalism', '0001', 7, 5, 'English'),
	('Chemestry', '0011', 8, 5, 'Science'),
	('Physics', '0011', 9, 5, 'Science'),
	('Geology', '0011', 10, 5, 'Science');

-- Create Course Goals
INSERT INTO course_goals VALUES ('Computers', 1),
				('Arithmetic', 2),
				('Writing', 5),
				('Reading', 6),
				('Journalism', 7),
				('Chemestry', 8),
				('Physics', 9),
				('Geology', 10);

-- Create Course Reqs
INSERT INTO curric_reqs VALUES ('Computers', 'Computer Science'),
				('Computers', 'Science'),
				('Computers', 'Math'),
				('Writing', 'Computer Science'),
				('Writing', 'Science'),
				('Writing', 'Math'),
				('Writing', 'English'),
				('Reading', 'English'),
				('Reading', 'Science'),
				('Arithmetic', 'Math'),
				('Arithmetic', 'Science'),
				('Arithmetic', 'English'),
				('Arithmetic', 'Computer Science'),
				('Statistics', 'Math'),
				('Statistics', 'Science'),
				('Calculus', 'Math'),
				('Calculus', 'Science'),
				('Calculus', 'Computer Science'),
				('Journalism', 'English'),
				('Chemestry', 'Science'),
				('Physics', 'Science'), 
				('Geology', 'Science');

-- Create Course Options
INSERT INTO curric_ops VALUES ('Reading', 'Computer Science'),
				('Reading', 'Math'),
				('Statistics', 'Computer Science'),
				('Calculus', 'English'),
				('Journalism', 'Science'),
				('Chemestry', 'Math'),
				('Physics', 'Math'),
				('Geology', 'Math');

--  Create Sections
INSERT INTO section VALUES (1, 'Computers', 'FALL', 0000, 20, 'no', 'comment'),
			(2, 'Computers', 'WINTER', 0000, 21, 'no', 'comment'),
			(3, 'Computers', 'SPRING', 0000, 22, 'no', 'comment'),
			(4, 'Computers', 'SUMMER', 0000, 23, 'no', 'comment'),
			(5, 'Computers', 'WINTER', 0001, 22, 'no', 'comment'),
			(6, 'Computers', 'SPRING', 0001, 21, 'no', 'comment'),
			(7, 'Computers', 'SUMMER', 0001, 20, 'no', 'comment'),
			(8, 'Writing', 'WINTER', 0000, 21, 'no', 'comment'),
			(9, 'Writing', 'SPRING', 0000, 22, 'no', 'comment'),
			(10, 'Writing', 'SUMMER', 0000, 23, 'no', 'comment'),
			(11, 'Writing', 'WINTER', 0001, 22, 'no', 'comment'),
			(12, 'Writing', 'SPRING', 0001, 21, 'no', 'comment'),
			(13, 'Writing', 'SUMMER', 0001, 20, 'no', 'comment'),
			(14, 'Reading', 'WINTER', 0000, 21, 'no', 'comment'),
			(15, 'Reading', 'SPRING', 0000, 22, 'no', 'comment'),
			(16, 'Reading', 'SUMMER', 0000, 23, 'no', 'comment'),
			(17, 'Reading', 'WINTER', 0001, 22, 'no', 'comment'),
			(18, 'Reading', 'SPRING', 0001, 21, 'no', 'comment'),
			(19, 'Reading', 'SUMMER', 0001, 20, 'no', 'comment'),
			(20, 'Arithmetic', 'WINTER', 0000, 21, 'no', 'comment'),
			(21, 'Arithmetic', 'SPRING', 0000, 22, 'no', 'comment'),
			(22, 'Arithmetic', 'SUMMER', 0000, 23, 'no', 'comment'),
			(23, 'Arithmetic', 'WINTER', 0001, 22, 'no', 'comment'),
			(24, 'Arithmetic', 'SPRING', 0001, 21, 'no', 'comment'),
			(25, 'Arithmetic', 'SUMMER', 0001, 20, 'no', 'comment'),
			(26, 'Statistics', 'WINTER', 0000, 21, 'no', 'comment'),
			(27, 'Statistics', 'SPRING', 0000, 22, 'no', 'comment'),
			(28, 'Statistics', 'SUMMER', 0000, 23, 'no', 'comment'),
			(29, 'Statistics', 'WINTER', 0001, 22, 'no', 'comment'),
			(30, 'Statistics', 'SPRING', 0001, 21, 'no', 'comment'),
			(31, 'Statistics', 'SUMMER', 0001, 20, 'no', 'comment'),
			(32, 'Calculus', 'SPRING', 0000, 22, 'no', 'comment'),
			(33, 'Calculus', 'SUMMER', 0000, 23, 'no', 'comment'),
			(34, 'Calculus', 'WINTER', 0001, 22, 'no', 'comment'),
			(35, 'Calculus', 'SPRING', 0001, 21, 'no', 'comment'),
			(36, 'Calculus', 'SUMMER', 0001, 20, 'no', 'comment'),
			(37, 'Journalism', 'WINTER', 0000, 21, 'no', 'comment'),
			(38, 'Journalism', 'SPRING', 0000, 22, 'no', 'comment'),
			(39, 'Journalism', 'SUMMER', 0000, 23, 'no', 'comment'),
			(40, 'Journalism', 'WINTER', 0001, 22, 'no', 'comment'),
			(41, 'Journalism', 'SPRING', 0001, 21, 'no', 'comment'),
			(42, 'Journalism', 'SUMMER', 0001, 20, 'no', 'comment'),
			(43, 'Chemestry', 'WINTER', 0000, 21, 'no', 'comment'),
			(44, 'Chemestry', 'SPRING', 0000, 22, 'no', 'comment'),
			(45, 'Chemestry', 'SUMMER', 0000, 23, 'no', 'comment'),
			(46, 'Chemestry', 'WINTER', 0001, 22, 'no', 'comment'),
			(47, 'Chemestry', 'SPRING', 0001, 21, 'no', 'comment'),
			(48, 'Chemestry', 'SUMMER', 0001, 20, 'no', 'comment'),
			(49, 'Physics', 'SPRING', 0000, 22, 'no', 'comment'),
			(50, 'Physics', 'SUMMER', 0000, 23, 'no', 'comment'),
			(51, 'Physics', 'WINTER', 0001, 22, 'no', 'comment'),
			(52, 'Physics', 'SPRING', 0001, 21, 'no', 'comment'),
			(53, 'Physics', 'SUMMER', 0001, 20, 'no', 'comment'),
			(54, 'Geology', 'SPRING', 0000, 22, 'no', 'comment'),
			(55, 'Geology', 'SUMMER', 0000, 23, 'no', 'comment'),
			(56, 'Geology', 'WINTER', 0001, 22, 'no', 'comment'),
			(57, 'Geology', 'SPRING', 0001, 21, 'no', 'comment'),
			(58, 'Geology', 'SUMMER', 0001, 20, 'no', 'comment');

-- Create Topics
INSERT INTO topic VALUES (1, 'Computers', 1, '0000', 5),
			(2, 'Writing', 1, '0001', 10),
			(3, 'Reading', 2, '0001', 5),
			(4, 'Math1', 1, '0010', 5),
			(5, 'Math2', 2, '0010', 5),
			(6, 'Math3', 3, '0010', 5),
			(7, 'Science1', 1, '0011', 5),
			(8, 'Science21', 2, '0011', 5),
			(9, 'Science22', 2, '0011', 10),
			(10, 'Science31', 3, '0011', 5),
			(11, 'Science32', 3, '0011', 10);

-- Create Topic_Currics
INSERT INTO topic_curric VALUES (1, 'Computer Science'),
				(1, 'Math'),
				(1, 'Science'),
				(2, 'Computer Science'),
				(2, 'English'),
				(2, 'Science'),
				(3, 'English'),
				(4, 'Computer Science'),
				(4, 'Math'),
				(4, 'Science'),
				(4, 'English'),
				(5, 'Math'),
				(5, 'Science'),
				(6, 'Math'),
				(6, 'Science'),
				(7, 'Science'),
				(7, 'Math'),
				(7, 'English'),
				(8, 'Math'),
				(9, 'Science'),
				(10, 'Computer Science'),
				(11, 'Science');

-- Create Goal Grades
INSERT INTO goal_grades VALUES (1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(7, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14);



-- Create Section Grades
INSERT INTO sec_grades VALUES (1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(7, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(13, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(16, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(21, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(22, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(26, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(27, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(29, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(31, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(32, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(33, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(34, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(35, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(36, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(37, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(38, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(39, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(40, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(41, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(42, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(43, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(44, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(45, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(46, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(47, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(48, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(49, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(50, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(51, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(52, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(53, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(54, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(55, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(56, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(57, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
			(58, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14);
      
UPDATE curriculum SET person_name = 'Grant' WHERE curric_name = 'C';
            
            
SELECT * FROM curriculum;
SELECT * FROM curric_reqs;
SELECT * FROM courses;
SELECT * FROM section;
SELECT * FROM sec_grades;


