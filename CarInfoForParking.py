from tkinter import font
import tkinter
from datetime import datetime, date


# class for getting all car information
class Enter_car(object):

    def carInfoFrame(self):

        # frame for getting all car information from user
        self.f3 = tkinter.Frame()
        self.f3.place(x=0, y=0, width=640, height=480)
        self.f3.config(bg='#FA8072')

        label = tkinter.Label(self.f3, text="Parking Ticket Information", bg='#FFDAB9')
        label.grid(row=0, column=1, sticky='w')
        label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

        # label and entry for car number
        carNumberLabel = tkinter.Label(self.f3, text="Car Number : ", width=20, bg='#FFDAB9')
        carNumberLabel.grid(row=1, column=0, sticky='ne')
        carNumberLabel['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')
        self.carNumberEntry = tkinter.Entry(self.f3)
        self.carNumberEntry.grid(row=1, column=1, sticky='n')

        # label and entry for car color
        carColorLabel = tkinter.Label(self.f3, text="Car Color : ", width=20, bg='#FFDAB9')
        carColorLabel.grid(row=2, column=0, sticky='ne')
        carColorLabel['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')
        self.carColorEntry = tkinter.Entry(self.f3)
        self.carColorEntry.grid(row=2, column=1, sticky='n')

        # label and entry for car type
        carTypeLabel = tkinter.Label(self.f3, text="  Car Type :  ", width=20, bg='#FFDAB9')
        carTypeLabel.grid(row=3, column=0, sticky='ne')
        carTypeLabel['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')
        self.carTypeEntry = tkinter.Entry(self.f3)
        self.carTypeEntry.grid(row=3, column=1, sticky='n')

        # label and entry for card type
        cardTypeLabel = tkinter.Label(self.f3, text="  Card Type :  ", width=20, bg='#FFDAB9')
        cardTypeLabel.grid(row=4, column=0, sticky='ne')
        cardTypeLabel['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')
        self.cardTypeEntry = tkinter.Entry(self.f3)
        self.cardTypeEntry.grid(row=4, column=1, sticky='n')

        # label and entry for card number
        cardNumberLabel = tkinter.Label(self.f3, text="  Card Number :  ", width=20, bg='#FFDAB9')
        cardNumberLabel.grid(row=5, column=0, sticky='ne')
        cardNumberLabel['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')
        self.cardNumberEntry = tkinter.Entry(self.f3)
        self.cardNumberEntry.grid(row=5, column=1, sticky='n')

        ok = tkinter.Button(self.f3, text="Ok", bg='#FF7F50', activebackground='#FFA500',
                            command=self.CheckInfo)
        ok.grid(row=5, column=1, sticky='e')

        cancel = tkinter.Button(self.f3, text="Cancel", bg='#FF7F50', activebackground='#FFA500',
                                command=self.f3.destroy)
        cancel.grid(row=5, column=2, sticky='w')

        self.f3.rowconfigure(0, weight=1)
        self.f3.rowconfigure(1, weight=1)
        self.f3.rowconfigure(2, weight=1)
        self.f3.rowconfigure(3, weight=1)
        self.f3.rowconfigure(4, weight=1)
        self.f3.rowconfigure(5, weight=2)

        self.f3.columnconfigure(0, weight=1)
        self.f3.columnconfigure(1, weight=1)
        self.f3.columnconfigure(2, weight=1)

    # methode for showing an warning
    def smallWindow(self):

        self.window = tkinter.Tk()
        self.window.title("PARKING LOT")
        self.window.geometry("200x100-200-400")
        self.window.config(bg="#FA8072")

        label = tkinter.Label(self.window, text="WARNING!", bg='#FA8072')
        label.pack(side='top')
        label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

        label2 = tkinter.Label(self.window, text='Please Enter all information.', bg='#FA8072')
        label2.pack(side='top')

        # ok button for destroy frame
        ok = tkinter.Button(self.window, text="OK", bg='#FF7F50', activebackground='#FFA500',
                            command=self.window.destroy)
        ok.pack(side='bottom', anchor='n')
        ok['font'] = tkinter.font.Font(size=15)
        ok['padx'] = 20

        self.window.minsize(200, 100)
        self.window.maxsize(200, 100)
        self.window.mainloop()

    # check methode for checking all information of car
    def CheckInfo(self):
        if self.carColorEntry.get() and self.carTypeEntry.get() and self.carNumberEntry.get() and self.cardTypeEntry.get() and self.cardNumberEntry.get():
            self.info()
            return self.ParkingTicket()
        else:
            return self.smallWindow()

    # methode for assigned all info
    def info(self):
        self.carNumber = self.carNumberEntry.get()
        self.carType = self.carTypeEntry.get()
        self.carColor = self.carColorEntry.get()
        self.cardType = self.cardTypeEntry.get()
        self.cardNumber = self.cardNumberEntry.get()

    def getCarNum(self):
        return self.carNumber

    def getCarType(self):
        return self.carType

    def getCarColor(self):
        return self.carColor

    # methode for show user parking ticket
    def ParkingTicket(self):

        now = datetime.now()
        self.carNum = self.getCarNum()
        self.carType = self.getCarType()
        self.carColor = self.getCarColor()

        arr1 = ['\tCar Number', '\tCar Type', '\tCar Color', '\tParking Date', '\tParking Time']
        arr2 = [self.carNum, self.carType, self.carColor, date.today(), now.strftime('%H:%M %p')]

        # frame for parking ticket
        self.f4 = tkinter.Frame()
        self.f4.place(x=0, y=0, width=640, height=480)
        self.f4.config(bg='#FA8072')

        label = tkinter.Label(self.f4, text='Parking Ticket', bg='#FFDAB9')
        label.grid(row=0, column=1, sticky='we')
        label['padx'] = 100
        label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

        # frame for show all parking ticket info on frame f4
        la = tkinter.Frame(self.f4)
        la.place(x=140, y=90, width=330, height=240)
        la.config(bg='#90EE90')
        la['padx'] = 8

        # show all information on parking ticket
        for i in range(5):
            text = tkinter.Label(la, text=arr1[i], bg='#90EE90')
            text.grid(row=i, column=0, sticky='w')
            text['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')

            colon = tkinter.Label(la, text=':', bg='#90EE90')
            colon.grid(row=i, column=1, sticky='w')
            colon['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')

            data = tkinter.Label(la, text=arr2[i], bg='#90EE90')
            data.grid(row=i, column=2, sticky='w')
            data['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')

        #  configure the row of frame la
        for i in range(5):
            la.rowconfigure(i, weight=1)

        # configure the column of frame la
        la.columnconfigure(0, weight=1)
        la.columnconfigure(1, weight=1)
        la.columnconfigure(2, weight=3)

        # ok button on f4 frame
        okButton = tkinter.Button(self.f4, text='Ok', bg='#FF7F50', activebackground='#FFA500',
                                  command=self.destroyFrame)
        okButton.grid(row=2, column=2, sticky='nw')
        # print button on f4 frame
        printButton = tkinter.Button(self.f4, text='Print', bg='#FF7F50', activebackground='#FFA500')
        printButton.grid(row=2, column=1, sticky='ne')

        # configure the row of frame f4
        self.f4.rowconfigure(0, weight=1)
        self.f4.rowconfigure(1, weight=2)
        self.f4.rowconfigure(2, weight=1)

        # configure the column of frame f4
        self.f4.columnconfigure(0, weight=1)
        self.f4.columnconfigure(1, weight=2)
        self.f4.columnconfigure(2, weight=1)

    # destroy Frame f4 and f3
    def destroyFrame(self):
        self.f4.destroy()
        self.f3.destroy()

    # Store Information in Data base
    def storeInfoInDB(self):
        pass
