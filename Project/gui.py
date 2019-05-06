## GUI file

import tkinter as tk
import tkinter.messagebox
import insert_data as ins
import queries as q

HEIGHT = 800
WIDTH = 800

#attr = 0

CURRIC_ATTR = ['curric_name', 'person_id', 'person_name', 'min_hours']
COURSE_ATTR = ['course_name', 'subj_code', 'course_no', 'cred_hrs', 'description']
CURRIC_REQS_ATTR = ['course_name', 'req_for']
CURRIC_OPS_ATTR = ['course_name', 'op_for']
TOPIC_ATTR = ['topic_id', 'topic_name', 'lvl', 'subject', 'units']
TOPIC_CURRIC_ATTR = ['topic_id', 'curric_assoc']
GOALS_ATTR = ['goal_id', 'description', 'curric_name']
SECTION_ATTR = ['section_id', 'course_name', 'semester', 'year', 'num_stu', 'comment1', 'comment2']
#SEC_GRADES_ATTR = ['']
#GOAL_GRADES_ATTR = []
COURSE_GOALS_ATTR = ['course_name', 'goal_id']

class MyGUI:
    def __init__(self, mycursor, mydb):
        self.cursor = mycursor
        self.db = mydb
        self.attr = 0

        self.new_curric_data = {}
        self.new_course_data = {}
        self.new_curric_reqs_data = {}
        self.new_curric_ops_data = {}
        self.new_topic_data = {}
        self.new_topic_curric_data = {}
        self.new_goals_data = {}
        self.new_section_data = {}
        self.new_course_goals_data = {}

        self.main_window = tk.Tk()

        self.main_window.title('Curriculum Database Application')

        self.main_window.geometry('1100x750')

        self.show_tables_button = tk.Button(self.main_window, text='Show Tables', font='10', command=lambda: self.show_tables())
        self.show_tables_button.place(relx=.13, rely=.05, relwidth=.2, relheight=.05)

        self.tables_label = tk.Label(self.main_window, anchor='nw', font=('Times', '10'))
        self.tables_label.place(relx= .13, rely = .11, relwidth=1, relheight=.1)


        self.top_label = tk.Label(self.main_window, anchor='nw', font=('Times', '12'))
        self.top_label.place(relx=0.5, rely=0.17, relwidth=0.75, relheight=0.05, anchor='n')
        self.top_label['text'] = 'Input New Data'

        self.top_frame = tk.Frame(self.main_window, bg='#a3a3c2', bd=2)
        self.top_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.2, anchor='n')



        #Create Menu in top frame for input new data, horrible syntax
        self.input_menu_button = tk.Menubutton(self.top_frame, text='Tables')
        self.input_menu_button.menu = tk.Menu(self.input_menu_button, tearoff=0)
        self.input_menu_button['menu'] = self.input_menu_button.menu


        #May have to create options dynamically (or could just hard code...)
        self.input_menu_button.menu.add_command(label='curriculum', command=lambda:self.display_text('curriculum'))
        self.input_menu_button.menu.add_command(label='courses', command=lambda:self.display_text('courses'))
        self.input_menu_button.menu.add_command(label='topic', command=lambda:self.display_text('topic'))
        self.input_menu_button.menu.add_command(label='curric_reqs', command=lambda:self.display_text('curric_reqs'))
        self.input_menu_button.menu.add_command(label='curric_ops', command=lambda:self.display_text('curric_ops'))
        self.input_menu_button.menu.add_command(label='topic_curric', command=lambda:self.display_text('topic_curric'))
        self.input_menu_button.menu.add_command(label='goals', command=lambda:self.display_text('goals'))
        self.input_menu_button.menu.add_command(label='section', command=lambda:self.display_text('section'))
        self.input_menu_button.menu.add_command(label='course_goals', command=lambda:self.display_text('course_goals'))
        self.input_menu_button.menu.add_command(label='Get Curriculum', command=lambda:self.get_curric())#CHANGE
        self.input_menu_button.place(relwidth=0.15, relheight=.2)

        self.mid_label = tk.Label(self.main_window, anchor='nw', font=('Times', '12'))
        self.mid_label.place(relx=0.5, rely=0.42, relwidth=0.75, relheight=0.05, anchor='n')
        self.mid_label['text'] = 'Update Existing Data'

        self.mid_frame = tk.Frame(self.main_window, bg='#a3a3c2', bd=2)
        self.mid_frame.place(relx=.5, rely=.45, relwidth=.75, relheight=0.2, anchor='n')


        self.bottom_label = tk.Label(self.main_window, anchor='nw', font=('Times', '12'))
        self.bottom_label.place(relx=0.5, rely=0.67, relwidth=0.75, relheight=0.05, anchor='n')
        self.bottom_label['text'] = 'Query Existing Data'

        self.bottom_frame = tk.Frame(self.main_window, bg='#a3a3c2', bd=2)
        self.bottom_frame.place(relx=.5, rely=.7, relwidth=.75, relheight=0.2, anchor='n')


        #run
        self.main_window.mainloop()



    def show_tables(self):
        self.cursor.execute('show tables')

        self.tables_label ['text'] = 'EXISTING TABLES: '
        i = 0
        for table in self.cursor:
            if i != 0:
                self.tables_label ['text'] += ', '

            self.tables_label ['text'] += table[0]
            i += 1


    def click_input_option(self, tbl_name):
        print('You clicked ' + tbl_name)


    def display_text(self, table_name):
        self.attr = 0

        self.insert_label = tk.Label(self.top_frame, font=('Times', '12'))
        self.insert_label.place(relx =.5, rely=.3, relwidth=0.25, relheight=.15)
        self.insert_label['text'] = 'Please enter ' + table_name + ' data.'

        self.insert_label_attr = tk.Label(self.top_frame, font=('Times', '12'))
        self.insert_label_attr.place(relx =.5, rely=.55, relwidth=0.2, relheight=.15)

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
        elif table_name == 'course_goals':
            self.insert_label_attr['text'] = 'Please enter ' + COURSE_GOALS_ATTR[self.attr]
            table_dict = COURSE_GOALS_ATTR


        self.entry = tk.Entry(self.top_frame, font=40)
        self.entry.place(relx =.5, rely=.75, relwidth=0.2, relheight=.2)

        self.button = tk.Button(self.top_frame, text="Enter", font=40, command=lambda: [self.insert_data(self.entry.get(), table_name, table_dict), self.change_attr(table_name, table_dict)])
        self.button.place(relx=0.75, rely=.75, relwidth=0.2, relheight=0.2)

    def change_attr(self, table_name, table_dict):
        self.attr += 1

        if self.attr < len(table_dict):
            self.insert_label_attr.destroy()
            self.entry.destroy()
            self.button.destroy()

            #change attribute that we are collecting
            self.insert_label_attr = tk.Label(self.top_frame, font=('Times', '12'))
            self.insert_label_attr.place(relx =.5, rely=.55, relwidth=0.2, relheight=.15)
            self.insert_label_attr['text'] = 'Please enter ' + table_dict[self.attr]

            #reset entry
            self.entry = tk.Entry(self.top_frame, font=40)
            self.entry.place(relx =.5, rely=.75, relwidth=0.2, relheight=.2)

            #reset button
            self.button = tk.Button(self.top_frame, text="Enter", font=40, command=lambda: [self.insert_data(self.entry.get(), table_name, table_dict), self.change_attr(table_name, table_dict)])
            self.button.place(relx=0.75, rely=.75, relwidth=0.2, relheight=0.2)

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
            elif table_name == 'course_goals':
                ins.insert_into_course_goals(self.new_course_goals_data, self.cursor, self.db)


    #FUNCTIONS FOR INSERTING DATA
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
        elif table_name == 'course_goals':
            self.new_course_goals_data[table_dict[self.attr]] = input


        #destroy
        #self.insert_label.destroy()
        #self.insert_label_attr.destroy()
        #self.entry.destroy()
        #self.button.destroy()




#--------------------------------------------------------------------------
    #FUNCTIONS FOR QUERIES
    def get_curric(self):

        #hardcode
        curric_name = 'Computer Science'
        person_id = '12345'

        result = q.get_curric(curric_name, person_id, self.cursor)

        for tuple in result:
            print(tuple)
