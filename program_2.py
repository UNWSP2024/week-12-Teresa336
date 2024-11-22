# Programmer: Teresa Fischer
# Date: 11/22/24
# Program # 2: Joe's Automotive

import tkinter

class ServicesGUI:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Joe\'s Automotive')
        # create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # label for instructions
        self.intro_label = tkinter.Label(self.top_frame, text='- Services at Joe\'s Automotive -')
        self.intro_label.pack(side='left')

        # create IntVar object for each checkbutton
        self.checkVar1 = tkinter.IntVar()
        self.checkVar2 = tkinter.IntVar()
        self.checkVar3 = tkinter.IntVar()
        self.checkVar4 = tkinter.IntVar()
        self.checkVar5 = tkinter.IntVar()
        self.checkVar6 = tkinter.IntVar()
        self.checkVar7 = tkinter.IntVar()

        # checkbuttons
        self.cb_1 = tkinter.Checkbutton(self.middle_frame, text='Oil Change - $30.00', variable=self.checkVar1, onvalue=30, offvalue=0)
        self.cb_2 = tkinter.Checkbutton(self.middle_frame, text='Lube Job - $20.00', variable=self.checkVar2, onvalue=20, offvalue=0)
        self.cb_3 = tkinter.Checkbutton(self.middle_frame, text='Radiator Flush - $40.00', variable=self.checkVar3, onvalue=40, offvalue=0)
        self.cb_4 = tkinter.Checkbutton(self.middle_frame, text='Transmission Fluid - $100.00', variable=self.checkVar4, onvalue=100, offvalue=0)
        self.cb_5 = tkinter.Checkbutton(self.middle_frame, text='Inspection - $35.00', variable=self.checkVar5, onvalue=35, offvalue=0)
        self.cb_6 = tkinter.Checkbutton(self.middle_frame, text='Muffler Replacement - $200.00', variable=self.checkVar6, onvalue=200, offvalue=0)
        self.cb_7 = tkinter.Checkbutton(self.middle_frame, text='Tire Rotation - $20.00', variable=self.checkVar7, onvalue=20, offvalue=0)

        # pack the check buttons
        self.cb_1.pack(side='top')
        self.cb_2.pack(side='top')
        self.cb_3.pack(side='top')
        self.cb_4.pack(side='top')
        self.cb_5.pack(side='top')
        self.cb_6.pack(side='top')
        self.cb_7.pack(side='top')

        # result variable and label
        self.value = tkinter.IntVar()
        self.total_label = tkinter.Label(self.bottom_frame, textvariable=self.value)
        self.result_button = tkinter.Button(self.bottom_frame, text='Calculate Charges', command=self.totals)
        self.result_label = tkinter.Label(self.bottom_frame, text='Total Charges: $')
        self.result_label.pack(side='left')
        self.total_label.pack(side='left')
        self.result_button.pack(side='top')

        # pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # enter the main loop
        tkinter.mainloop()

    def totals(self):
        total = 0
        for var in (self.checkVar1, self.checkVar2, self.checkVar3, self.checkVar4, self.checkVar5, self.checkVar6, self.checkVar7):
            total += var.get()
        self.value.set(int(total))


# instance of Services GUI
if __name__ == '__main__':
    services_gui = ServicesGUI()