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

class MyGUI:
    def __init__(self, mycursor, mydb):
        self.cursor = mycursor
        self.db = mydb
        self.attr = 0

        self.new_curric_data = {}


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
        self.input_menu_button.menu.add_command(label='Curriculum', command=lambda:self.display_curric_text())
        self.input_menu_button.menu.add_command(label='Courses', command=lambda:self.insert_course())
        self.input_menu_button.menu.add_command(label='Get Curriculum', command=lambda:self.get_curric())#CHANGE
        self.input_menu_button.place(relwidth=0.15, relheight=.2)

        self.mid_label = tk.Label(self.main_window, anchor='nw', font=('Times', '12'))
        self.mid_label.place(relx=0.5, rely=0.42, relwidth=0.75, relheight=0.05, anchor='n')
        self.mid_label['text'] = 'Edit Existing Data'

        self.mid_frame = tk.Frame(self.main_window, bg='#a3a3c2', bd=2)
        self.mid_frame.place(relx=.5, rely=.45, relwidth=.75, relheight=0.2, anchor='n')


        self.bottom_label = tk.Label(self.main_window, anchor='nw', font=('Times', '12'))
        self.bottom_label.place(relx=0.5, rely=0.67, relwidth=0.75, relheight=0.05, anchor='n')
        self.bottom_label['text'] = 'Query Existing Data'

        self.bottom_frame = tk.Frame(self.main_window, bg='#a3a3c2', bd=2)
        self.bottom_frame.place(relx=.5, rely=.7, relwidth=.75, relheight=0.2, anchor='n')

        #self.lower_frame = tk.Frame(self.main_window, bg='#ff33cc', bd=5)
        #self.lower_frame.place(relx=0.5, rely=.7, relwidth=0.75, relheight=0.35, anchor='s')

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


    #def get_input(self,input):
    #    print(input)


    def click_input_option(self, tbl_name):
        print('You clicked ' + tbl_name)


    def display_curric_text(self):
        self.attr = 0

        self.insert_label = tk.Label(self.top_frame, font=('Times', '12'))
        self.insert_label.place(relx =.5, rely=.3, relwidth=0.25, relheight=.15)
        self.insert_label['text'] = 'Please enter Curriculum data.'

        self.insert_label_attr = tk.Label(self.top_frame, font=('Times', '12'))
        self.insert_label_attr.place(relx =.5, rely=.55, relwidth=0.2, relheight=.15)
        self.insert_label_attr['text'] = 'Please enter ' + CURRIC_ATTR[self.attr]

        self.entry = tk.Entry(self.top_frame, font=40)
        self.entry.place(relx =.5, rely=.75, relwidth=0.2, relheight=.2)

        self.button = tk.Button(self.top_frame, text="Enter", font=40, command=lambda: [self.insert_curric_data(self.entry.get()), self.change_attr()])
        self.button.place(relx=0.75, rely=.75, relwidth=0.2, relheight=0.2)

    def change_attr(self):
        self.attr += 1

        if self.attr < len(CURRIC_ATTR):
            self.insert_label_attr.destroy()
            self.entry.destroy()
            self.button.destroy()

            #change attribute that we are collecting
            self.insert_label_attr = tk.Label(self.top_frame, font=('Times', '12'))
            self.insert_label_attr.place(relx =.5, rely=.55, relwidth=0.2, relheight=.15)
            self.insert_label_attr['text'] = 'Please enter ' + CURRIC_ATTR[self.attr]

            #reset entry
            self.entry = tk.Entry(self.top_frame, font=40)
            self.entry.place(relx =.5, rely=.75, relwidth=0.2, relheight=.2)

            #reset button
            self.button = tk.Button(self.top_frame, text="Enter", font=40, command=lambda: [self.insert_curric_data(self.entry.get()), self.change_attr()])
            self.button.place(relx=0.75, rely=.75, relwidth=0.2, relheight=0.2)

        #cannot accept any more values, so insert into table
        else:
            #Insert data into db
            ins.insert_into_curric(self.new_curric_data, self.cursor, self.db)


    #FUNCTIONS FOR INSERTING DATA
    def insert_curric_data(self, input):
        print(input)

        #Just hardcode for now
        self.new_curric_data[CURRIC_ATTR[self.attr]] = input

        #destroy
        #self.insert_label.destroy()
        #self.insert_label_attr.destroy()
        #self.entry.destroy()
        #self.button.destroy()



    def insert_course(self):
        print('Insert Course data')

        new_course_data = {}

        self.insert_label = tk.Label(self.top_frame, font=('Times', '12'))
        self.insert_label.place(relx =.5, rely=.3, relwidth=0.25, relheight=.15)
        self.insert_label['text'] = 'Please enter Course data.'


        for attr in COURSE_ATTR:

            self.insert_label_attr = tk.Label(self.top_frame, font=('Times', '12'))
            self.insert_label_attr.place(relx =.5, rely=.55, relwidth=0.2, relheight=.15)
            self.insert_label_attr['text'] = 'Please enter ' + attr

            self.entry = tk.Entry(self.top_frame, font=40)
            self.entry.place(relx =.5, rely=.75, relwidth=0.2, relheight=.2)

            self.button = tk.Button(self.top_frame, text="Enter", font=40, command=lambda: print('placeholder'))
            self.button.place(relx=0.75, rely=.75, relwidth=0.2, relheight=0.2)

        #Just hardcode for now
        new_course_data[CURRIC_ATTR[0]] = 'Database'
        new_course_data[CURRIC_ATTR[1]] = 'CSI'
        new_course_data[CURRIC_ATTR[2]] = '3335'
        new_course_data[CURRIC_ATTR[3]] = 3
        new_course_data[CURRIC_ATTR[4]] = 'Not a fun class'

        #destroy
        #self.insert_label.destroy()
        #self.insert_label_attr.destroy()
        #self.entry.destroy()
        #self.button.destroy()

        #Insert data into db
        ins.insert_into_curric(new_curric_data, self.cursor, self.db)



#--------------------------------------------------------------------------
    #FUNCTIONS FOR QUERIES
    def get_curric(self):

        #hardcode
        curric_name = 'Computer Science'
        person_id = '12345'

        result = q.get_curric(curric_name, person_id, self.cursor)

        for tuple in result:
            print(tuple)
