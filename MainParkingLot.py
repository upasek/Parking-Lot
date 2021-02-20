import tkinter
from tkinter import font
import CarInfoForParking
from CarInfoForExit import ExitCarInfo


class parkingLot(object):

    def __init__(self):
        # main Window frame
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("PARKING LOT SYSTEM")
        self.mainWindow.geometry("640x480-8-200")
        self.mainWindow.config(bg='#FA8072')

        # label on main window
        label = tkinter.Label(self.mainWindow, text="PARKING LOT SYSTEM", bg='#FFDAB9')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

        ob = CarInfoForParking.Enter_car()
        # button for enter your car on self.mainWindow
        EnterCar = tkinter.Button(self.mainWindow, text='Enter Car', bg='#FF7F50', activebackground='#FFA500',
                                  command=ob.carInfoFrame)
        EnterCar.grid(row=1, column=1, sticky='w')
        EnterCar['font'] = tkinter.font.Font(size=15)

        # button for exit your car on self.mainWindow
        ob2 = ExitCarInfo()
        ExitCar = tkinter.Button(self.mainWindow, text='Exit Car', bg='#FF7F50', activebackground='#FFA500',
                                 command=ob2.ExitCar)
        ExitCar.grid(row=1, column=1, sticky='e')
        ExitCar['font'] = tkinter.font.Font(size=15)

        # configure column
        self.mainWindow.columnconfigure(0, weight=1)
        self.mainWindow.columnconfigure(1, weight=1)
        self.mainWindow.columnconfigure(2, weight=1)

        # configure row for main window frame
        self.mainWindow.rowconfigure(0, weight=1)
        self.mainWindow.rowconfigure(1, weight=1)
        self.mainWindow.rowconfigure(2, weight=1)

        # max and min size of frame
        self.mainWindow.minsize(640, 480)
        self.mainWindow.maxsize(640, 480)

        self.mainWindow.mainloop()


if __name__ == '__main__':
    p = parkingLot()
