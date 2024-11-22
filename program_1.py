# Programmer: Teresa Fischer
# Date: 11/22/24
# Program # 1: MPG Calculator

import tkinter

class MpgGUI:
    def __init__(self):
        self.gallons = None
        self.miles_per_gallon = None
        self.miles = None
        self.main_window = tkinter.Tk()
        self.main_window.title('Miles Per Gallon Calculator')

        # create frames
        self.frame_1 = tkinter.Frame(self.main_window)
        self.frame_2 = tkinter.Frame(self.main_window)
        self.frame_3 = tkinter.Frame(self.main_window)
        self.frame_4 = tkinter.Frame(self.main_window)

        # label and entry box for gallons
        self.gallons_label = tkinter.Label(self.frame_1, text='Enter the amount of gas the car holds (in gallons):')
        self.gallons_entry = tkinter.Entry(self.frame_1)
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        # label and entry box for miles
        self.miles_label = tkinter.Label(self.frame_2, text='Enter the number of miles the car can be driven on a full tank:')
        self.miles_entry = tkinter.Entry(self.frame_2)
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # results
        self.result_label = tkinter.Label(self.frame_3, text='Miles Per Gallon:')
        self.value = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.frame_3, textvariable=self.value)
        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')

        # calculate button
        self.mpg_button = tkinter.Button(self.frame_4, text='Calculate MPG', command=self.calculate_mpg)
        self.mpg_button.pack(side='left')

        # quit button
        self.quit_button = tkinter.Button(self.frame_4, text='Quit', command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        # pack the frames
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()

        # enter the mainloop
        tkinter.mainloop()

    # calculate mpg
    def calculate_mpg(self):
        self.gallons = float(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())
        self.miles_per_gallon = self.miles / self.gallons
        self.value.set(str(round(self.miles_per_gallon, 2)))


# instance of MpgGUI
if __name__ == '__main__':
    mpg_gui = MpgGUI()