# Programmer: Teresa Fischer
# Date: 11/22/24
# Program # 3: Long-Distance Calls

import tkinter
import tkinter.messagebox

class CallsGUI:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Long-Distance Calls')

        # create frames
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)

        # create IntVar object for radiobuttons
        self.radio_var = tkinter.DoubleVar()

        # create radio button widgets
        self.rb1 = tkinter.Radiobutton(self.frame2, text='Daytime (6:00 A.M. through 5:59 P.M.) - $0.02',
                                        variable=self.radio_var, value=0.02)
        self.rb2 = tkinter.Radiobutton(self.frame2, text='Evening (6:00 P.M.  through 11:59 P.M.) - $0.12',
                                        variable=self.radio_var, value=0.12)
        self.rb3 = tkinter.Radiobutton(self.frame2, text='Off-Peak (midnight through 5:59 P.M.) - $0.05',
                                        variable=self.radio_var, value=0.05)

        # pack the raidobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # entry label and box
        self.minutes_label = tkinter.Label(self.frame3, text='Enter the number of minutes of the call:')
        self.minutes_entry = tkinter.Entry(self.frame3)

        # pack the entry label and box
        self.minutes_label.pack(side='left')
        self.minutes_entry.pack(side='left')

        # calculate button and quit button
        self.calc_button = tkinter.Button(self.frame4, text='Calculate Charges', command=self.show_charges)
        self.quit_button = tkinter.Button(self.frame4, text='Quit', command=self.main_window.destroy)

        # pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        # main loop
        tkinter.mainloop()

    def show_charges(self):
        charge = 0
        self.minutes = float(self.minutes_entry.get())
        self.price = float(self.radio_var.get())
        charge = self.minutes*self.price
        tkinter.messagebox.showinfo('Long-Distance Calls', 'Your total charges for your long distance call are $%s' %charge)


# instance of Calls GUI
if __name__ == '__main__':
    calls_gui = CallsGUI()