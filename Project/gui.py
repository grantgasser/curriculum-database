## GUI file

import tkinter as tk
import tkinter.messagebox

HEIGHT = 800
WIDTH = 800

class MyGUI:
    def __init__(self, mycursor):
        self.cursor = mycursor


        self.main_window = tk.Tk()

        self.main_window.title('Curriculum Database Application')

        self.main_window.geometry('800x600')

        self.frame = tk.Frame(self.main_window, bg='blue', bd=2)
        self.frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.3, anchor='n')

        self.entry = tk.Entry(self.frame, font=40)
        self.entry.place(relwidth=0.65, relheight=.8)

        self.button = tk.Button(self.frame, text="Input Data", font=40, command=lambda: self.show_tables(self.entry.get()))
        self.button.place(relx=0.7, relheight=1, relwidth=0.3)

        self.lower_frame = tk.Frame(self.main_window, bg='blue', bd=5)
        self.lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')

        self.label = tk.Label(self.lower_frame)
        self.label.place(rely = .1, relwidth=1, relheight=.9)


        # Pack the frames.
        #self.top_frame.pack()
        #self.mid_frame.pack()
        #self.bottom_frame.pack()

        #run
        self.main_window.mainloop()


    #TODO: put in the GUI
    def show_tables(self, input):
        #self.cursor.execute('show tables')

        #for table in self.cursor:
        #    print(table[0])

        self.label['text'] = input


    #FUNCTIONS FOR INSERTING DATA
    def enter_curric(self):
        pass



    #FUNCTIONS FOR QUERIES
    def get_curric(self):
        pass
