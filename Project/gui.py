######################################################################################
# Authors: Grant Gasser, Jackson O'Donnell
#
# Purpose: Provide a GUI for our project
######################################################################################

import tkinter as tk
import tkinter.messagebox
import insert_data as ins
import queries as q
import upadte_data as up

HEIGHT = 800
WIDTH = 800

#attr = 0

CURRIC_ATTR = ['curric_name', 'person_name', 'person_id', 'min_hours', 'min_cover2', 'min_cover3']
COURSE_ATTR = ['course_name', 'subj_code', 'course_no', 'cred_hrs', 'description']
CURRIC_REQS_ATTR = ['course_name', 'req_for']
CURRIC_OPS_ATTR = ['course_name', 'op_for']
TOPIC_ATTR = ['topic_id', 'topic_name', 'subject', 'units']
TOPIC_CURRIC_ATTR = ['topic_id', 'curric_assoc', 'lvl']
GOALS_ATTR = ['goal_id', 'description', 'curric_name', 'goal_hrs']
SECTION_ATTR = ['course_name', 'section_id', 'course_name', 'semester', 'year', 'num_stu', 'comment1', 'comment2']
SEC_GRADES_ATTR = ['section_id', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'I', 'W']
GOAL_GRADES_ATTR = ['goal_id', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'I', 'W']
COURSE_GOALS_ATTR = ['course_name', 'goal_id']
COURSE_TOPIC_ATTR = ['course_name', 'topic_id']

#keys
CURRIC_KEYS = ['curric_name', 'Attribute:', 'New Value:']
COURSE_KEYS = ['course_name', 'Attribute:', 'New Value:']
CURRIC_REQS_KEYS = ['course_name', 'req_for', 'Attribute:', 'New Value:']
CURRIC_OPS_KEYS = ['course_name', 'op_for', 'Attribute:', 'New Value:']
TOPIC_KEYS = ['topic_name', 'topic_id', 'Attribute:', 'New Value:']
TOPIC_CURRIC_KEYS = ['topic_id', 'curric_assoc', 'lvl', 'Attribute:', 'New Value:']
GOALS_KEYS = ['goal_id', 'Attribute:', 'New Value:']
SECTION_KEYS = ['section_id', 'Attribute:', 'New Value:']
SEC_GRADES_KEYS = ['course_name', 'section_id', 'Attribute:', 'New Value:']
GOAL_GRADES_KEYS = ['goal_id', 'Attribute:', 'New Value:']
COURSE_GOALS_KEYS = ['goal_id', 'course_name', 'Attribute:', 'New Value:']
COURSE_TOPIC_KEYS = ['course_name', 'topic_id', 'Attribute:', 'New Value:']


class MyGUI:
    def __init__(self, mycursor, mydb):
        self.cursor = mycursor
        self.db = mydb
        self.attr = 0
        self.curric_keys = 0

        #for inserting data
        self.new_curric_data = {}
        self.new_course_data = {}
        self.new_curric_reqs_data = {}
        self.new_curric_ops_data = {}
        self.new_topic_data = {}
        self.new_topic_curric_data = {}
        self.new_goals_data = {}
        self.new_section_data = {}
        self.new_course_goals_data = {}
        self.new_sec_grades_data = {}
        self.new_goal_grades_data = {}
        self.new_course_topic_data = {}

        #for update data
        self.update_curric_data = {}
        self.update_course_data = {}
        self.update_curric_reqs_data = {}
        self.update_curric_ops_data = {}
        self.update_topic_data = {}
        self.update_topic_curric_data = {}
        self.update_goals_data = {}
        self.update_section_data = {}
        self.update_course_goals_data = {}
        self.update_sec_grades_data = {}
        self.update_goal_grades_data = {}
        self.update_course_topic_data = {}

        #for querying data
        self.curric_key_input = [] #user will enter keys, stored here
        self.update_attr_input = []

        self.main_window = tk.Tk()

        #self.background_image = tk.PhotoImage(file='background.jpg')
        #self.background_label = tk.Label(root, image=background_image)
        #self.background_label.place(relwidth=1, relheight=1)

        self.main_window.title('Curriculum Database Application')

        self.main_window.geometry('1100x750')

        ##################
        # SHOW TABLES
        self.show_tables_button = tk.Button(self.main_window, text='Show Tables', font='10', command=lambda: self.show_tables())
        self.show_tables_button.place(relx=.13, rely=.05, relwidth=.2, relheight=.05)

        self.tables_label = tk.Label(self.main_window, anchor='nw', font=('Times', '10'))
        self.tables_label.place(relx= .13, rely = .11, relwidth=1, relheight=.1)
        ##################


        self.top_label = tk.Label(self.main_window, anchor='nw', font=('Times', '12'))
        self.top_label.place(relx=0.25, rely=0.17, relwidth=0.25, relheight=0.03, anchor='n')
        self.top_label['text'] = 'Input New Data'

        self.top_frame = tk.Frame(self.main_window, bg='#a3a3c2', bd=2)
        self.top_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.2, anchor='n')


        ##################
        # INSERT DATA

        #Create Menu in top frame for input new data, horrible syntax
        self.input_menu_button = tk.Menubutton(self.top_frame, text='Tables')
        self.input_menu_button.menu = tk.Menu(self.input_menu_button, tearoff=0)
        self.input_menu_button['menu'] = self.input_menu_button.menu


        #Dropdown Menu options
        self.input_menu_button.menu.add_command(label='curriculum', command=lambda:self.display_text('curriculum'))
        self.input_menu_button.menu.add_command(label='courses', command=lambda:self.display_text('courses'))
        self.input_menu_button.menu.add_command(label='topic', command=lambda:self.display_text('topic'))
        self.input_menu_button.menu.add_command(label='curric_reqs', command=lambda:self.display_text('curric_reqs'))
        self.input_menu_button.menu.add_command(label='curric_ops', command=lambda:self.display_text('curric_ops'))
        self.input_menu_button.menu.add_command(label='topic_curric', command=lambda:self.display_text('topic_curric'))
        self.input_menu_button.menu.add_command(label='goals', command=lambda:self.display_text('goals'))
        self.input_menu_button.menu.add_command(label='section', command=lambda:self.display_text('section'))
        self.input_menu_button.menu.add_command(label='course_goals', command=lambda:self.display_text('course_goals'))
        self.input_menu_button.menu.add_command(label='sec_grades', command=lambda:self.display_text('sec_grades'))
        self.input_menu_button.menu.add_command(label='goal_grades', command=lambda:self.display_text('goal_grades'))
        self.input_menu_button.menu.add_command(label='course_topic', command=lambda:self.display_text('course_topic'))

        #Place menu
        self.input_menu_button.place(relwidth=0.15, relheight=.2)

        self.mid_label = tk.Label(self.main_window, anchor='nw', font=('Times', '12'))
        self.mid_label.place(relx=0.5, rely=0.42, relwidth=0.75, relheight=0.05, anchor='n')
        self.mid_label['text'] = 'Query Existing Data'

        self.mid_frame = tk.Frame(self.main_window, bg='#a3a3c2', bd=2)
        self.mid_frame.place(relx=.5, rely=.45, relwidth=.75, relheight=0.27, anchor='n')
        ##################

        ##################
        # QUERY CURRICULUM DASHBOARD
        self.top_curric_dash_label = tk.Label(self.main_window, anchor='nw', font=('Times', '12'))
        self.top_curric_dash_label.place(relx=0.8, rely=0.17, relwidth=0.3, relheight=0.03, anchor='n')
        self.top_curric_dash_label['text'] = 'Curriculum Dashboard'

        self.top_curric_dash_label = tk.Label(self.top_frame, anchor='n', font=('Times', '12'))
        self.top_curric_dash_label.place(relx=.65, rely=0, relwidth=.15, relheight=0.15, anchor='n')
        self.top_curric_dash_label['text'] = 'Enter curric_name: '

        self.top_curric_dash_label_entry  = tk.Entry(self.top_frame, font=25)
        self.top_curric_dash_label_entry .place(relx=.74, rely=0, relwidth=.17, relheight=.15)

        self.top_curric_dash_label_button = tk.Button(self.top_frame, text='Go', font= 25, command=lambda:print('click'))
        self.top_curric_dash_label_button.place(relx=.92, rely=0, relwidth = .06, relheight=.15)

        #################

        ##################
        # QUERY CURRICULUM
        self.mid_curric_label = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_curric_label.place(relx=.10, rely=0, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_curric_label['text'] = 'Query Curriculum Data'

        self.mid_curric_label_attr = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_curric_label_attr.place(relx=.10, rely=.15, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_curric_label_attr['text'] = 'Enter curric_name'

        self.mid_curric_entry = tk.Entry(self.mid_frame, font=25)
        self.mid_curric_entry.place(relx=0, rely=.30, relwidth=.2, relheight=.15)

        self.mid_curric_button = tk.Button(self.mid_frame, text='Go', font= 25, command=lambda:self.curric_query(self.mid_curric_entry.get()))
        self.mid_curric_button.place(relx=.21, rely=.30, relwidth = .06, relheight=.15)
        #################

        ##################
        # QUERY COURSE
        self.mid_course_label = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_course_label.place(relx=.41, rely=0, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_course_label['text'] = 'Query Course Data'

        self.mid_course_label_attr = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_course_label_attr.place(relx=.41, rely=.15, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_course_label_attr['text'] = 'Enter course_name'

        self.mid_course_label_entry  = tk.Entry(self.mid_frame, font=25)
        self.mid_course_label_entry .place(relx=.31, rely=.30, relwidth=.2, relheight=.15)

        self.mid_course_label_button = tk.Button(self.mid_frame, text='Go', font= 25, command=lambda:[self.course_query(self.mid_course_label_entry.get()), self.reset_course_query()])
        self.mid_course_label_button.place(relx=.52, rely=.30, relwidth = .06, relheight=.15)
        #################

        ##################
        # QUERY CURRICULUM-COURSE (GET SECTION AND GRADE DIST)
        self.course_curric_attr = ['curric_name', 'year1', 'year2']
        self.course_curric_attr_num = 0
        self.course_curric_vals = {}

        self.mid_course_curric_label = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_course_curric_label.place(relx=.7, rely=0, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_course_curric_label['text'] = 'Get Section Grade Dist.'

        self.mid_course_curric_label_attr = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_course_curric_label_attr.place(relx=.7, rely=.15, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_course_curric_label_attr['text'] = 'Enter curric_name'

        self.mid_course_curric_label_entry  = tk.Entry(self.mid_frame, font=25)
        self.mid_course_curric_label_entry .place(relx=.6, rely=.30, relwidth=.2, relheight=.15)

        self.mid_course_curric_label_button = tk.Button(self.mid_frame, text='Go', font= 25, command=lambda:[self.course_curric_query(self.mid_course_curric_label_entry.get()), self.next_input()])
        self.mid_course_curric_label_button.place(relx=.81, rely=.30, relwidth = .06, relheight=.15)
        #################

        #################
        # QUERY 4
        self.course_curric_attr = ['curric_name', 'course_name', 'year1', 'year2', 'semester1',
                                'semester2', 'semester3', 'semester4']
        self.course_curric_attr_num = 0
        self.course_curric_vals = {}

        self.mid_course_curric_label = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_course_curric_label.place(relx=.41, rely=.5, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_course_curric_label['text'] = 'Get Curriculum Grade Dist.'

        self.mid_course_curric_label_attr = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_course_curric_label_attr.place(relx=.41, rely=.65, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_course_curric_label_attr['text'] = 'Enter curric_name'

        self.mid_course_curric_label_entry  = tk.Entry(self.mid_frame, font=25)
        self.mid_course_curric_label_entry .place(relx=.31, rely=.8, relwidth=.2, relheight=.15)

        self.mid_course_curric_label_button = tk.Button(self.mid_frame, text='Go', font= 25, command=lambda:[self.course_curric_query(self.mid_course_curric_label_entry.get()), self.next_input()])
        self.mid_course_curric_label_button.place(relx=.52, rely=.8, relwidth = .06, relheight=.15)
        #################
        
        #################
        # QUERY 5
        self.course_curric_attr = ['curric_name', 'course_name', 'year1', 'year2']
        self.course_curric_attr_num = 0
        self.course_curric_vals = {}

        self.mid_course_curric_label = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_course_curric_label.place(relx=.7, rely=.5, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_course_curric_label['text'] = 'Get Section Grade Dist.'

        self.mid_course_curric_label_attr = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_course_curric_label_attr.place(relx=.7, rely=.65, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_course_curric_label_attr['text'] = 'Enter curric_name'

        self.mid_course_curric_label_entry  = tk.Entry(self.mid_frame, font=25)
        self.mid_course_curric_label_entry .place(relx=.6, rely=.8, relwidth=.2, relheight=.15)

        self.mid_course_curric_label_button = tk.Button(self.mid_frame, text='Go', font= 25, command=lambda:[self.course_curric_query(self.mid_course_curric_label_entry.get()), self.next_input()])
        self.mid_course_curric_label_button.place(relx=.81, rely=.8, relwidth = .06, relheight=.15)


        #################

        ##################
        # UPDATE DATA
        self.bottom_label = tk.Label(self.main_window, anchor='nw', font=('Times', '12'))
        self.bottom_label.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.05, anchor='n')
        self.bottom_label['text'] = 'Update Existing Data'

        self.bottom_frame = tk.Frame(self.main_window, bg='#a3a3c2', bd=2)
        self.bottom_frame.place(relx=.5, rely=.78, relwidth=.75, relheight=0.2, anchor='n')

        #Create Menu in top frame for input new data, horrible syntax
        self.update_menu_button = tk.Menubutton(self.bottom_frame, text='Tables')
        self.update_menu_button.menu = tk.Menu(self.update_menu_button, tearoff=0)
        self.update_menu_button['menu'] = self.update_menu_button.menu


        #Dropdown Menu options
        self.update_menu_button.menu.add_command(label='curriculum', command=lambda:self.display_text_update('curriculum'))
        self.update_menu_button.menu.add_command(label='courses', command=lambda:self.display_text_update('courses'))
        self.update_menu_button.menu.add_command(label='topic', command=lambda:self.display_text_update('topic'))
        self.update_menu_button.menu.add_command(label='curric_reqs', command=lambda:self.display_text_update('curric_reqs'))
        self.update_menu_button.menu.add_command(label='curric_ops', command=lambda:self.display_text_update('curric_ops'))
        self.update_menu_button.menu.add_command(label='topic_curric', command=lambda:self.display_text_update('topic_curric'))
        self.update_menu_button.menu.add_command(label='goals', command=lambda:self.display_text_update('goals'))
        self.update_menu_button.menu.add_command(label='section', command=lambda:self.display_text_update('section'))
        self.update_menu_button.menu.add_command(label='course_goals', command=lambda:self.display_text_update('course_goals'))
        self.update_menu_button.menu.add_command(label='sec_grades', command=lambda:self.display_text_update('sec_grades'))
        self.update_menu_button.menu.add_command(label='goal_grades', command=lambda:self.display_text_update('goal_grades'))
        self.update_menu_button.menu.add_command(label='course_topic', command=lambda:self.display_text_update('course_topic'))

        #Place menu
        self.update_menu_button.place(relwidth=0.15, relheight=.2)


        self.update_attr = 0
        #################

        #run
        self.main_window.mainloop()


#--------------------------------------------------------------------------
    #FUNCTIONS FOR INSERTING DATA

    #shows the existing tables in the schema at top of screen
    def show_tables(self):
        self.cursor.execute('show tables')

        self.tables_label ['text'] = 'EXISTING TABLES: '
        i = 0
        for table in self.cursor:
            if i != 0:
                self.tables_label ['text'] += ', '

            self.tables_label ['text'] += table[0]
            i += 1


    #displays text in top frame for inputting data
    def display_text(self, table_name):
        self.attr = 0

        self.insert_label = tk.Label(self.top_frame, font=('Times', '12'))
        self.insert_label.place(relx =.2, rely=.2, relwidth=0.25, relheight=.15)
        self.insert_label['text'] = 'Please enter ' + table_name + ' data.'

        self.insert_label_attr = tk.Label(self.top_frame, font=('Times', '12'))
        self.insert_label_attr.place(relx =.2, rely=.45, relwidth=0.25, relheight=.15)

        table_dict = {}
        if table_name == 'curriculum':
            self.insert_label_attr['text'] = 'Please enter ' + CURRIC_ATTR[self.attr]
            table_dict = CURRIC_ATTR
        elif table_name == 'courses':
            self.insert_label_attr['text'] = 'Please enter ' + COURSE_ATTR[self.attr]
            table_dict = COURSE_ATTR
        elif table_name == 'curric_reqs':
            self.insert_label_attr['text'] = 'Please enter ' + CURRIC_REQS_ATTR[self.attr]
            table_dict = CURRIC_REQS_ATTR
        elif table_name == 'curric_ops':
            self.insert_label_attr['text'] = 'Please enter ' + CURRIC_OPS_ATTR[self.attr]
            table_dict = CURRIC_OPS_ATTR
        elif table_name == 'topic':
            self.insert_label_attr['text'] = 'Please enter ' + TOPIC_ATTR[self.attr]
            table_dict = TOPIC_ATTR
        elif table_name == 'topic_curric':
            self.insert_label_attr['text'] = 'Please enter ' + TOPIC_CURRIC_ATTR[self.attr]
            table_dict = TOPIC_CURRIC_ATTR
        elif table_name == 'goals':
            self.insert_label_attr['text'] = 'Please enter ' + GOALS_ATTR[self.attr]
            table_dict = GOALS_ATTR
        elif table_name == 'section':
            self.insert_label_attr['text'] = 'Please enter ' + SECTION_ATTR[self.attr]
            table_dict = SECTION_ATTR
        elif table_name == 'sec_grades':
            self.insert_label_attr['text'] = 'Please enter ' + SEC_GRADES_ATTR[self.attr]
            table_dict = SEC_GRADES_ATTR
        elif table_name == 'goal_grades':
            self.insert_label_attr['text'] = 'Please enter ' + GOAL_GRADES_ATTR[self.attr]
            table_dict = GOAL_GRADES_ATTR
        elif table_name == 'course_goals':
            self.insert_label_attr['text'] = 'Please enter ' + COURSE_GOALS_ATTR[self.attr]
            table_dict = COURSE_GOALS_ATTR
        elif table_name == 'course_topic':
            self.insert_label_attr['text'] = 'Please enter ' + COURSE_TOPIC_ATTR[self.attr]
            table_dict = COURSE_TOPIC_ATTR

            


        self.entry = tk.Entry(self.top_frame, font=25)
        self.entry.place(relx =.2, rely=.7, relwidth=0.2, relheight=.2)

        self.button = tk.Button(self.top_frame, text="Enter", font=40, command=lambda: [self.insert_data(self.entry.get(), table_name, table_dict), self.change_attr(table_name, table_dict)])
        self.button.place(relx=0.41, rely=.71, relwidth=0.12, relheight=0.2)

    def change_attr(self, table_name, table_dict):
        self.attr += 1

        if self.attr < len(table_dict):
            self.insert_label_attr.destroy()
            self.entry.destroy()
            self.button.destroy()

            #change attribute that we are collecting
            self.insert_label_attr = tk.Label(self.top_frame, font=('Times', '12'))
            self.insert_label_attr.place(relx =.2, rely=.45, relwidth=0.25, relheight=.15)
            self.insert_label_attr['text'] = 'Please enter ' + table_dict[self.attr]

            #reset entry
            self.entry = tk.Entry(self.top_frame, font=25)
            self.entry.place(relx =.2, rely=.7, relwidth=0.2, relheight=.2)

            #reset button
            self.button = tk.Button(self.top_frame, text="Enter", font=40, command=lambda: [self.insert_data(self.entry.get(), table_name, table_dict), self.change_attr(table_name, table_dict)])
            self.button.place(relx=0.41, rely=.71, relwidth=0.12, relheight=0.2)

        #cannot accept any more values, so insert into table
        else:
            #Insert data into db
            if table_name == 'curriculum':
                ins.insert_into_curric(self.new_curric_data, self.cursor, self.db)
            elif table_name == 'courses':
                ins.insert_into_courses(self.new_course_data, self.cursor, self.db)
            elif table_name == 'curric_reqs':
                ins.insert_into_reqs(self.new_curric_reqs_data, self.cursor, self.db)
            elif table_name == 'curric_ops':
                ins.insert_into_ops(self.new_curric_ops_data, self.cursor, self.db)
            elif table_name == 'topic':
                ins.insert_into_topic(self.new_topic_data, self.cursor, self.db)
            elif table_name == 'topic_curric':
                ins.insert_into_topic_curric(self.new_topic_curric_data, self.cursor, self.db)
            elif table_name == 'goals':
                ins.insert_into_goals(self.new_goals_data, self.cursor, self.db)
            elif table_name == 'section':
                ins.insert_into_section(self.new_section_data, self.cursor, self.db)
            elif table_name == 'sec_grades':
                ins.insert_into_sec_grades(self.new_sec_grades_data, self.cursor, self.db)
            elif table_name == 'goal_grades':
                ins.insert_into_goal_grades(self.new_goal_grades_data, self.cursor, self.db)
            elif table_name == 'course_goals':
                ins.insert_into_course_goals(self.new_course_goals_data, self.cursor, self.db)
            elif table_name == 'course_topic':
                ins.insert_into_course_topic(self.new_course_topic_data, self.cursor, self.db)

            #RESET
            self.update_curric_data = {}
            self.update_course_data = {}
            self.update_curric_reqs_data = {}
            self.update_curric_ops_data = {}
            self.update_topic_data = {}
            self.update_topic_curric_data = {}
            self.update_goals_data = {}
            self.update_section_data = {}
            self.update_course_goals_data = {}
            self.update_sec_grades_data = {}
            self.update_goal_grades_data = {}
            self.update_course_topic_data = {}



    def insert_data(self, input, table_name, table_dict):
        print(input)

        #Just hardcode for now
        if table_name == 'curriculum':
            self.new_curric_data[table_dict[self.attr]] = input
        elif table_name == 'courses':
            self.new_course_data[table_dict[self.attr]] = input
        elif table_name == 'curric_reqs':
            self.new_curric_reqs_data[table_dict[self.attr]] = input
        elif table_name == 'curric_ops':
            self.new_curric_ops_data[table_dict[self.attr]] = input
        elif table_name == 'topic':
            self.new_topic_data[table_dict[self.attr]] = input
        elif table_name == 'topic_curric':
            self.new_topic_curric_data[table_dict[self.attr]] = input
        elif table_name == 'goals':
            self.new_goals_data[table_dict[self.attr]] = input
        elif table_name == 'section':
            self.new_section_data[table_dict[self.attr]] = input
        elif table_name == 'sec_grades':
            self.new_sec_grades_data[table_dict[self.attr]] = input
        elif table_name == 'goal_grades':
            self.new_goal_grades_data[table_dict[self.attr]] = input
        elif table_name == 'course_goals':
            self.new_course_goals_data[table_dict[self.attr]] = input
        elif table_name == 'course_goals':
            self.new_course_topic_data[table_dict[self.attr]] = input




#--------------------------------------------------------------------------
    #FUNCTIONS FOR QUERIES
    def course_curric_query(self, input):
        if self.course_curric_attr_num < 4:
            self.course_curric_vals[self.course_curric_attr[self.course_curric_attr_num]] = input

            self.course_curric_attr_num += 1

            #finished getting values, execute query and display
            if self.course_curric_attr_num == 4:
                print(self.course_curric_vals)
                self.course_curric_attr_num = 0


                #reset button
                self.mid_course_curric_label_button.destroy()
                self.mid_course_curric_label_button = tk.Button(self.mid_frame, text='Go', font= 25, command=lambda:[self.course_curric_query(self.mid_course_curric_label_entry.get()), self.next_input()])
                self.mid_course_curric_label_button.place(relx=.81, rely=.30, relwidth = .06, relheight=.15)

                #run query
                print('\nGetting section(s) grade distribution(s)...')
                section_grade_dist = q.get_section(self.course_curric_vals[self.course_curric_attr[0]], self.course_curric_vals[self.course_curric_attr[1]],
                                                    self.course_curric_vals[self.course_curric_attr[2]], self.course_curric_vals[self.course_curric_attr[3]],
                                                    self.cursor)

                #SEC_GRADES_ATTR
                for tuple in section_grade_dist:
                    print('\n')
                    i = 0
                    for attr in SEC_GRADES_ATTR:
                        print(attr + ': ' + str(tuple[i]))
                        i +=  1

                self.mid_course_curric_notif = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
                self.mid_course_curric_notif.place(relx=.75, rely=.6, relwidth=.25, relheight=0.12, anchor='n')
                self.mid_course_curric_notif['text'] = 'Check the console for the result.'




    def next_input(self):
        #print('next attribute')

        #Ask for new attr value
        self.mid_course_curric_label_attr.destroy()


        self.mid_course_curric_label_attr = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.mid_course_curric_label_attr.place(relx=.7, rely=.15, relwidth=.2, relheight=0.12, anchor='n')
        self.mid_course_curric_label_attr['text'] = 'Enter ' + self.course_curric_attr[self.course_curric_attr_num]

        #Reset entry
        self.mid_course_curric_label_entry.destroy()
        self.mid_course_curric_label_entry  = tk.Entry(self.mid_frame, font=25)
        self.mid_course_curric_label_entry .place(relx=.6, rely=.30, relwidth=.2, relheight=.15)




    #runs the course query, displays data
    def course_query(self, input):
        #get course tuple
        course_tuple = q.get_course(input, self.cursor)
        print(course_tuple[0])

        #display course tuple to screen
        self.course_tup_result = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.course_tup_result.place(relx=.44, rely=.47, relwidth=.30, relheight=0.12, anchor='n')
        self.course_tup_result['text'] = str(course_tuple[0])

        #get curricula that course is required by
        course_reqs = q.get_reqs_given_course(input, self.cursor)

        reqs = []
        for tuple in course_reqs:
            print('Required by', tuple)
            reqs.append(tuple[0])


        #get curricula that course is optional for
        course_ops = q.get_ops_given_course(input, self.cursor)

        ops = []
        for tuple in course_ops:
            print('Optional for', tuple)
            ops.append(tuple[0])


        #display course-curricula data
        self.curric_topic = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.curric_topic.place(relx=0.30, rely=.63, relwidth = .3, relheight=.25)
        self.curric_topic['text'] = 'Required by: ' + str(reqs) + '\n Optional for: ' + str(ops)

    #resets entry field and button for course query
    def reset_course_query(self):
        self.mid_course_label_entry.destroy()

        self.mid_course_label_entry  = tk.Entry(self.mid_frame, font=25)
        self.mid_course_label_entry .place(relx=.31, rely=.30, relwidth=.2, relheight=.15)


    def curric_query(self, input):
        #print(input)
        self.curric_key_input.append(input)


        curric_info = q.get_curric(input, self.cursor)

        for tuple in curric_info:
            print('\nResult: ', tuple, '\n')
            tup_str = str(tuple)
            #print(tup_str)
            self.curric_tup_result = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
            self.curric_tup_result.place(relx=0.005, rely=.48, relwidth = .3, relheight=.12)
            self.curric_tup_result['text'] = tup_str

        #data from topic_curric table (topics associated w/ this curric)
        topic_curric = q.get_topic_curric(input, self.cursor)

        topics = []
        for tuple in topic_curric:
            print('Topic:', tuple)
            topics.append(tuple[0])


        #data from curric_reqs (required courses for given curric)
        curric_reqs = q.get_reqs_given_curric(input, self.cursor)

        reqs = []
        for tuple in curric_reqs:
            print('Required Course(s):', tuple)
            reqs.append(tuple[0])

        #data from curric_ops (optional courses for given curric)
        curric_ops = q.get_ops_given_curric(input, self.cursor)

        ops = []
        for tuple in curric_ops:
            print('Optional Course(s):', tuple)
            ops.append(tuple[0])

        #show results on GUI
        self.curric_topic = tk.Label(self.mid_frame, anchor='n', font=('Times', '12'))
        self.curric_topic.place(relx=0.005, rely=.63, relwidth = .3, relheight=.33)
        self.curric_topic['text'] = 'Topics: ' + str(topics) + '\n Opt Course(s): ' + str(ops) + '\n Req Course(s): ' + str(reqs)





#--------------------------------------------------------------------------
    #FUNCTIONS FOR UPDATE DATA

    #displays text in top frame for inputting data
    def display_text_update(self, table_name):
        self.update_attr = 0

        #display direction and label
        self.update_label = tk.Label(self.bottom_frame, font=('Times', '12'))
        self.update_label.place(relx =.2, rely=0, relwidth=0.55, relheight=.15)
        self.update_label['text'] = 'Please enter the attribute of ' + table_name + ' that you want to change.'

        self.update_label_attr = tk.Label(self.bottom_frame, font=('Times', '12'))
        self.update_label_attr.place(relx =.2, rely=.2, relwidth=0.15, relheight=.2)


        table_list = []
        if table_name == 'curriculum':
            self.update_label_attr['text'] = CURRIC_KEYS[self.update_attr]
            table_list = CURRIC_KEYS
        elif table_name == 'courses':
            self.update_label_attr['text'] = COURSE_KEYS[self.update_attr]
            table_list = COURSE_KEYS
        elif table_name == 'curric_reqs':
            self.update_label_attr['text'] = CURRIC_REQS_KEYS[self.update_attr]
            table_list = CURRIC_REQS_KEYS
        elif table_name == 'curric_ops':
            self.update_label_attr['text'] = CURRIC_OPS_KEYS[self.update_attr]
            table_list = CURRIC_OPS_KEYS
        elif table_name == 'topic':
            self.update_label_attr['text'] = TOPIC_KEYS[self.update_attr]
            table_list = TOPIC_KEYS
        elif table_name == 'topic_curric':
            self.update_label_attr['text'] = TOPIC_CURRIC_KEYS[self.update_attr]
            table_list = TOPIC_CURRIC_KEYS
        elif table_name == 'goals':
            self.update_label_attr['text'] = GOALS_KEYS[self.update_attr]
            table_list = GOALS_KEYS
        elif table_name == 'section':
            self.update_label_attr['text'] = SECTION_KEYS[self.update_attr]
            table_list = SECTION_KEYS
        elif table_name == 'sec_grades':
            self.update_label_attr['text'] = SEC_GRADES_KEYS[self.update_attr]
            table_list = SEC_GRADES_KEYS
        elif table_name == 'goal_grades':
            self.update_label_attr['text'] = GOAL_GRADES_KEYS[self.update_attr]
            table_list = GOAL_GRADES_KEYS
        elif table_name == 'course_goals':
            self.update_label_attr['text'] = COURSE_GOALS_KEYS[self.update_attr]
            table_list = COURSE_GOALS_KEYS
        elif table_name == 'course_topic':
            self.update_label_attr['text'] = COURSE_TOPIC_KEYS[self.update_attr]
            table_list = COURSE_TOPIC_KEYS




        #Display entry field and button
        self.update_entry = tk.Entry(self.bottom_frame, font=25)
        self.update_entry.place(relx =.36, rely=.2, relwidth=0.2, relheight=.2)

        self.button = tk.Button(self.bottom_frame, text="Enter", font=40, command=lambda: [self.update(self.update_entry.get(), table_name, table_list), self.next_update_attr(table_name, table_list)])
        self.button.place(relx=0.57, rely=.2, relwidth=0.12, relheight=0.2)


    def next_update_attr(self, table_name, table_list):
        self.update_attr += 1


        if self.update_attr < len(table_list):
            self.update_label_attr.destroy()
            self.update_entry.destroy()

            #ask for next attribute
            self.update_label_attr = tk.Label(self.bottom_frame, font=('Times', '12'))
            self.update_label_attr.place(relx =.2, rely=.2, relwidth=0.15, relheight=.2)
            self.update_label_attr['text'] = table_list[self.update_attr]

            #reset entry
            self.update_entry = tk.Entry(self.bottom_frame, font=25)
            self.update_entry.place(relx =.36, rely=.2, relwidth=0.2, relheight=.2)

            #reset button
            self.button = tk.Button(self.bottom_frame, text="Enter", font=40, command=lambda: [self.update(self.update_entry.get(), table_name, table_list), self.next_update_attr(table_name, table_list)])
            self.button.place(relx=0.57, rely=.2, relwidth=0.12, relheight=0.2)


        #run query
        else:
            if table_name == 'curriculum':
                print('Update data: ', self.update_curric_data)
                up.updateCurriculum(self.update_curric_data, self.cursor, self.db)
            elif table_name == 'courses':
                print('Update data: ', self.update_course_data)
                up.updateCourses(self.update_course_data, self.cursor, self.db)
            elif table_name == 'curric_reqs':
                print('Update data: ', self.update_course_data)
                up.updateReqs(self.update_course_data, self.cursor, self.db)
            elif table_name == 'curric_ops':
                print('Update data: ', self.update_curric_data)
                up.updateOps(self.update_curric_data, self.cursor, self.db)
            elif table_name == 'topic':
                print('Update data: ', self.update_topic_data)
                up.updateTopic(self.update_topic_data, self.cursor, self.db)
            elif table_name == 'topic_curric':
                print('Update data: ', self.update_topic_curric_data)
                up.updateTopicCurric(self.update_topic_curric_data, self.cursor, self.db)
            elif table_name == 'goals':
                print('Update data: ', self.update_goals_data)
                up.updateGoals(self.update_goals_data, self.cursor, self.db)
            elif table_name == 'section':
                print('Update data: ', self.update_section_data)
                up.updateSection(self.update_section_data, self.cursor, self.db)
            elif table_name == 'sec_grades':
                print('Update data: ', self.update_sec_grades_data)
                up.updateSecGrades(self.update_sec_grades_data, self.cursor, self.db)
            elif table_name == 'goal_grades':
                print('Update data: ', self.update_goal_grades_data)
                up.updateGoalGrades(self.update_goal_grades_data, self.cursor, self.db)
            elif table_name == 'course_goals':
                print('Update data: ', self.update_course_goals_data)
                up.updateReqs(self.update_course_goals_data, self.cursor, self.db)


            #AFTER UPDATE, RESET ENTRY AND BUTTON
            self.update_attr = 0

            #reset entry
            self.update_entry = tk.Entry(self.bottom_frame, font=25)
            self.update_entry.place(relx =.36, rely=.2, relwidth=0.2, relheight=.2)

            #reset button
            self.button = tk.Button(self.bottom_frame, text="Enter", font=40, command=lambda: [self.update(self.update_entry.get(), table_name, table_list), self.next_update_attr(table_name, table_list)])
            self.button.place(relx=0.57, rely=.2, relwidth=0.12, relheight=0.2)


    def update(self, input, table_name, table_list):
        #print(input)

        if table_name == 'curriculum':
            self.update_curric_data[table_list[self.update_attr]] = input
        elif table_name == 'courses':
            self.update_course_data[table_list[self.update_attr]] = input
        elif table_name == 'curric_reqs':
            self.update_curric_reqs_data[table_list[self.update_attr]] = input
        elif table_name == 'curric_ops':
            self.update_curric_ops_data[table_list[self.update_attr]] = input
        elif table_name == 'topic':
            self.update_topic_data[table_list[self.update_attr]] = input
        elif table_name == 'topic_curric':
            self.update_topic_curric_data[table_list[self.update_attr]] = input
        elif table_name == 'goals':
            self.update_goals_data[table_list[self.update_attr]] = input
        elif table_name == 'section':
            self.update_section_data[table_list[self.update_attr]] = input
        elif table_name == 'sec_grades':
            self.update_sec_grades_data[table_list[self.update_attr]] = input
        elif table_name == 'goal_grades':
            self.update_goal_grades_data[table_list[self.update_attr]] = input
        elif table_name == 'course_goals':
            self.update_course_goals_data[table_list[self.update_attr]] = input
