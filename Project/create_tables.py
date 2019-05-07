## File that creates the tables

def create_tables(mycursor):

    #mycursor.execute('show tables')

    mycursor.execute("DROP TABLE IF EXISTS curriculum")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `curriculum`(
            `curric_name` VARCHAR(25) NOT NULL,
            `person_name` VARCHAR(25) NOT NULL,
            `person_id` VARCHAR(25) NOT NULL,
            `min_hours` int NOT NULL CHECK (min_hours >= 0),
            `min_cover2` int NOT NULL CHECK (min_cover2 >= 0),
            `min_cover3` int NOT NULL CHECK (min_cover3 >= 0),
            PRIMARY KEY (`curric_name`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)

    mycursor.execute("DROP TABLE IF EXISTS `courses`")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `courses`(
            `course_name` VARCHAR(25) NOT NULL,
            `subj_code` VARCHAR(5) NOT NULL,
            `course_no` int NOT NULL CHECK (course_no >= 0),
            `cred_hrs` int NOT NULL CHECK (cred_hrs >= 0),
            `description` VARCHAR(255) NOT NULL,
            PRIMARY KEY (`course_name`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)

    mycursor.execute("DROP TABLE IF EXISTS `curric_reqs`")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `curric_reqs`(
            `course_name` VARCHAR(25) NOT NULL,
            `req_for` VARCHAR(25) NOT NULL,
            PRIMARY KEY (course_name, req_for),
            FOREIGN KEY (`course_name`) REFERENCES `courses`(`course_name`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)

    mycursor.execute("DROP TABLE IF EXISTS `curric_ops`")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `curric_ops`(
            `course_name` VARCHAR(25) NOT NULL,
            `op_for` VARCHAR(25) NOT NULL,
            PRIMARY KEY (course_name, op_for),
            FOREIGN KEY (`course_name`) REFERENCES `courses`(`course_name`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)

    mycursor.execute("DROP TABLE IF EXISTS `topic`")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `topic`(
            `topic_id` int NOT NULL CHECK (topic_id >= 0),
            `topic_name` VARCHAR(25) NOT NULL,
            `lvl` int NOT NULL CHECK (lvl >= 0 AND lvl < 4),
            `subject` VARCHAR(5) NOT NULL,
            `units` FLOAT NOT NULL,
            PRIMARY KEY(`topic_id`, `topic_name`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)

    mycursor.execute("DROP TABLE IF EXISTS `topic_curric`")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `topic_curric`(
            `topic_id` int NOT NULL CHECK (topic_id >= 0),
            `curric_assoc` VARCHAR(25) NOT NULL,
            PRIMARY KEY(topic_id, curric_assoc),
            FOREIGN KEY (`curric_assoc`) REFERENCES `curriculum`(`curric_name`),
            FOREIGN KEY (`topic_id`) REFERENCES `topic`(`topic_id`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)

    mycursor.execute("DROP TABLE IF EXISTS `goals`")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `goals`(
            `goal_id` int NOT NULL CHECK (goal_id >= 0),
            `description` VARCHAR(255) NOT NULL,
            `curric_name` VARCHAR(25) NOT NULL,
            `goal_hrs` int NOT NULL CHECK (goal_hrs >- 0),
            PRIMARY KEY (`goal_id`),
            FOREIGN KEY (`curric_name`) REFERENCES `curriculum`(`curric_name`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)

    mycursor.execute("DROP TABLE IF EXISTS `section`")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `section`(
            `section_id` int NOT NULL CHECK (section_id >= 0),
            `course_name` VARCHAR(25) NOT NULL,
            `semester` VARCHAR(7) NOT NULL,
            `year` int NOT NULL CHECK (year >= 0),
            `num_stu` int NOT NULL CHECK (num_stu >= 0),
            `comment1` VARCHAR(255) NOT NULL,
            `comment2` VARCHAR(255) NOT NULL,
            PRIMARY KEY (`section_id`),
            FOREIGN KEY (`course_name`) REFERENCES `courses`(`course_name`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)

    mycursor.execute("DROP TABLE IF EXISTS `sec_grades`")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `sec_grades`(
            `section_id` int NOT NULL CHECK (section_id >= 0),
            `A+` int NOT NULL CHECK (`A+` >= 0),
            `A` int NOT NULL CHECK (A >= 0),
            `A-` int NOT NULL CHECK (`A-` >= 0),
            `B+` int NOT NULL CHECK (`B+` >= 0),
            `B` int NOT NULL CHECK (B >= 0),
            `B-` int NOT NULL CHECK (`B-` >= 0),
            `C+` int NOT NULL CHECK (`C+` >= 0),
            `C` int NOT NULL CHECK (C >= 0),
            `C-` int NOT NULL CHECK (`C-` >= 0),
            `D+` int NOT NULL CHECK (`D+` >= 0),
            `D` int NOT NULL CHECK (D >= 0),
            `D-` int NOT NULL CHECK (`D-` >= 0),
            `F` int NOT NULL CHECK (F >= 0),
            `I` int NOT NULL CHECK (I >= 0),
            `W` int NOT NULL CHECK (W >= 0),
            PRIMARY KEY(`section_id`),
            FOREIGN KEY(`section_id`) REFERENCES `section`(`section_id`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)


    mycursor.execute("DROP TABLE IF EXISTS `goal_grades`")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `goal_grades`(
            `goal_id` int NOT NULL CHECK (goal_id >= 0),
            `A+` int NOT NULL CHECK (`A+` >= 0),
            `A` int NOT NULL CHECK (A >= 0),
            `A-` int NOT NULL CHECK (`A-` >= 0),
            `B+` int NOT NULL CHECK (`B+` >= 0),
            `B` int NOT NULL CHECK (B >= 0),
            `B-` int NOT NULL CHECK (`B-` >= 0),
            `C+` int NOT NULL CHECK (`C+` >= 0),
            `C` int NOT NULL CHECK (C >= 0),
            `C-` int NOT NULL CHECK (`C-` >= 0),
            `D+` int NOT NULL CHECK (`D+` >= 0),
            `D` int NOT NULL CHECK (D >= 0),
            `D-` int NOT NULL CHECK (`D-` >= 0),
            `F` int NOT NULL CHECK (F >= 0),
            `I` int NOT NULL CHECK (I >= 0),
            `W` int NOT NULL CHECK (W >= 0),
            PRIMARY KEY(`goal_id`),
            FOREIGN KEY(`goal_id`) REFERENCES `goals`(`goal_id`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)

    mycursor.execute("DROP TABLE IF EXISTS `course_goals`")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS `course_goals`(
            `course_name` VARCHAR(25) NOT NULL,
            `goal_id` int NOT NULL CHECK (goal_id >= 0),
            PRIMARY KEY (`course_name`, `goal_id`),
            FOREIGN KEY (`course_name`) REFERENCES `courses`(`course_name`),
            FOREIGN KEY (`goal_id`) REFERENCES `goals`(`goal_id`))
            ENGINE=InnoDB, DEFAULT CHARSET=latin1
            """)
