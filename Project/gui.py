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


        #TODO: put in the GUI 
    def show_tables(self):
        self.cursor.execute('show tables')

        for table in self.cursor:
            print(table[0])

#mygui = MyGUI()
