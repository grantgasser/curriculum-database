-- ------------------------------------------------------------------
-- Authors: Jackson O'Donnell, Zee Dugar, Grant Gasser
-- ------------------------------------------------------------------

-- ------------------------------------------------------------------
-- Make the database
-- ------------------------------------------------------------------

-- Make or remake curriculum database, then use it
DROP DATABASE IF EXISTS `curriculum_db`;
CREATE DATABASE IF NOT EXISTS `curriculum_db`;

USE `curriculum_db`;



-- ------------------------------------------------------------------
-- Make the relationships
-- ------------------------------------------------------------------

-- Make or remake curriculum relationship
DROP TABLE IF EXISTS `curriculum`;
CREATE TABLE IF NOT EXISTS `curriculum`(
   `curric_name` VARCHAR(25) NOT NULL,
   `person_name` VARCHAR(25) NOT NULL,
   `person_id` VARCHAR(25) NOT NULL,
   `min_hours` int NOT NULL,
   `topic_cat` VARCHAR(25) NOT NULL,
   PRIMARY KEY (`curric_name`, `person_id`))
   ENGINE=InnoDB, DEFAULT CHARSET=latin1;


-- Make or remake courses relationship 
DROP TABLE IF EXISTS `courses`;
CREATE TABLE IF NOT EXISTS `courses`(
   `course_name` VARCHAR(25) NOT NULL,
   `subj_code` VARCHAR(5) NOT NULL,
   `course_no` int NOT NULL,
   `cred_hrs` int NOT NULL,
   `description` VARCHAR(255) NOT NULL,
   PRIMARY KEY (`course_name`))  
   ENGINE=InnoDB, DEFAULT CHARSET=latin1;

-- Make or remake curric_courses relationship
DROP TABLE IF EXISTS `curric_courses`;
CREATE TABLE IF NOT EXISTS `curric_courses`(
   `course_name` VARCHAR(25) NOT NULL,
   `req_by` VARCHAR(25) NOT NULL,
   `op_for` VARCHAR(25) NOT NULL,
   PRIMARY KEY (`course_name`),
   FOREIGN KEY (`course_name`) REFERENCES `courses`(`course_name`))
   ENGINE=InnoDB, DEFAULT CHARSET=latin1;

-- Make or remake topic relationship
DROP TABLE IF EXISTS `topic`;
CREATE TABLE IF NOT EXISTS `topic`(
   `topic_id` int NOT NULL,
   `topic_name` VARCHAR(25) NOT NULL,
   `lvl` int NOT NULL,
   `subject` VARCHAR(25) NOT NULL,
   `units` FLOAT NOT NULL,
   `curric_assoc` VARCHAR(25) NOT NULL,
   PRIMARY KEY(`topic_id`, `topic_name`),
   FOREIGN KEY (`curric_assoc`) REFERENCES `curriculum`(`curric_name`))
   ENGINE=InnoDB, DEFAULT CHARSET=latin1;

-- Make or remake goals relationship
DROP TABLE IF EXISTS `goals`;
CREATE TABLE IF NOT EXISTS `goals`(
   `goal_id` int NOT NULL,
   `description` VARCHAR(255) NOT NULL,
   `curric_name` VARCHAR(25) NOT NULL,
   PRIMARY KEY (`goal_id`),
   FOREIGN KEY (`curric_name`) REFERENCES `curriculum`(`curric_name`))
   ENGINE=InnoDB, DEFAULT CHARSET=latin1;

-- Make or remake section relationship
DROP TABLE IF EXISTS `section`;
CREATE TABLE IF NOT EXISTS `section`(
   `section_id` int NOT NULL,
   `course_name` VARCHAR(25) NOT NULL,
   `semester` VARCHAR(7) NOT NULL,
   `num_stu` int NOT NULL,
   `comment1` VARCHAR(255) NOT NULL,
   `comment2` VARCHAR(255) NOT NULL,
   PRIMARY KEY (`section_id`),
   FOREIGN KEY (`course_name`) REFERENCES `courses`(`course_name`))
   ENGINE=InnoDB, DEFAULT CHARSET=latin1;

-- Make or remake grades relationship
DROP TABLE IF EXISTS `grades`;
CREATE TABLE IF NOT EXISTS `grades`(
   `section_id` int NOT NULL,
   `A+` int NOT NULL,
   `A` int NOT NULL,
   `A-` int NOT NULL,
   `B+` int NOT NULL,
   `B` int NOT NULL,
   `B-` int NOT NULL,
   `C+` int NOT NULL,
   `C` int NOT NULL,
   `C-` int NOT NULL,
   `D+` int NOT NULL,
   `D` int NOT NULL,
   `D-` int NOT NULL,
   `F` int NOT NULL,
   `I` int NOT NULL,
   `W` int NOT NULL,
   PRIMARY KEY(`section_id`),
   FOREIGN KEY(`section_id`) REFERENCES `section`(`section_id`))
   ENGINE=InnoDB, DEFAULT CHARSET=latin1;

--Make or remake course_goals relationship
DROP TABLE IF EXISTS `course_goals`;
CREATE TABLE IF NOT EXISTS `course_goals`(
   `course_name` VARCHAR(25) NOT NULL,
   `goal_id` int NOT NULL,
   PRIMARY KEY (`course_name`, `goal_id`),
   FOREIGN KEY (`course_name`) REFERENCES `courses`(`course_name`),
   FOREIGN KEY (`goal_id`) REFERENCES `goals`(`goal_id`))
   ENGINE=InnoDB, DEFAULT CHARSET=latin1;
