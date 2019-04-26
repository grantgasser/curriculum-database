## GUI file

import tkinter
import tkinter.messagebox

DAY_PRICE = .07
EVENING_PRICE = .12
OFF_PEAK_PRICE = .05

class MyGUI:
    def __init__(self):


        self.main_window = tkinter.Tk()


        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Daytime (6am-5:59pm): $.07/min',
                                       variable=self.radio_var,
                                       value=1)

        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Evening (6pm-11:59pm): $.12/min',
                                       variable=self.radio_var,
                                       value=2)

        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Off-Peak (12am-5:59am): $.05/min',
                                       variable=self.radio_var,
                                       value=3)

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create an OK button and a Quit button.
        self.ok_button = tkinter.Button(self.middle_frame,
                                        text='Enter',
                                        command=self.show_charge)
        self.quit_button = tkinter.Button(self.middle_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)


        # Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')


        # Pack the frames.
        self.top_frame.pack()
        self.middle_frame.pack()

        # Create the widgets for the bottom frame.
        self.prompt_label = tkinter.Label(self.top_frame,
                    text='Enter the number of minutes for the call:')
        self.minute_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.minute_entry.pack(side='left')


        # Start the mainloop.
        tkinter.mainloop()

    def show_charge(self):
        category = self.radio_var.get()

        if category == 1:
            price = DAY_PRICE #.07
        elif category == 2:
            price = EVENING_PRICE
        elif category == 3:
            price = OFF_PEAK_PRICE


        tkinter.messagebox.showinfo('Total Charge', 'The charge for the call is $' +
                                    str(price*float(self.minute_entry.get())))

mygui = MyGUI()
