## GUI file

import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self, mycursor):
        self.cursor = mycursor


        self.main_window = tk.Tk()

        self.main_window.title('Curriculum Database Application')

        self.main_window.geometry('500x300')


        #run
        self.main_window.mainloop()


    def show_tables(self):
        #lb = tk.Listbox(self.main_window)
        #lb.insert(1, 'Python')
        #lb.insert(2, 'Foo')

        #lb.pack()


        mycursor.execute('show tables')



        #for table in mycursor:


#mygui = MyGUI()
