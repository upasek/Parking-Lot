from tkinter import font
import tkinter
from datetime import datetime, date
import GenerateRandomInfo
import SendEmail


# class for getting all car information
class Enter_car(object):

    def __init__(self):
        self.carNumber = None
        self.carType = None
        self.carColor = None
        self.__cardType = None
        self.__cardNumber = None

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
        CN = GenerateRandomInfo.CarNumberRand()
        self.carNumberEntry.insert(0, CN)                                # insert an information in entry box
        self.carNumberEntry.grid(row=1, column=1, sticky='n')

        # label and entry for car color
        carColorLabel = tkinter.Label(self.f3, text="Car Color : ", width=20, bg='#FFDAB9')
        carColorLabel.grid(row=2, column=0, sticky='ne')
        carColorLabel['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')
        self.carColorEntry = tkinter.Entry(self.f3)
        CC = GenerateRandomInfo.CarColorRand()
        self.carColorEntry.insert(0, CC)                                 # insert an information in entry box
        self.carColorEntry.grid(row=2, column=1, sticky='n')

        # label and entry for car type
        carTypeLabel = tkinter.Label(self.f3, text="  Car Type :  ", width=20, bg='#FFDAB9')
        carTypeLabel.grid(row=3, column=0, sticky='ne')
        carTypeLabel['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')
        self.carTypeEntry = tkinter.Entry(self.f3)
        CT = GenerateRandomInfo.CarTypeRand()
        self.carTypeEntry.insert(0, CT)
        self.carTypeEntry.grid(row=3, column=1, sticky='n')

        # label and entry for card type
        cardTypeLabel = tkinter.Label(self.f3, text="  Card Type :  ", width=20, bg='#FFDAB9')
        cardTypeLabel.grid(row=4, column=0, sticky='ne')
        cardTypeLabel['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')
        self.cardTypeEntry = tkinter.Entry(self.f3)
        CardT = GenerateRandomInfo.getCardType()
        self.cardTypeEntry.insert(0, CardT)
        self.cardTypeEntry.grid(row=4, column=1, sticky='n')

        # label and entry for card number
        cardNumberLabel = tkinter.Label(self.f3, text="  Card Number :  ", width=20, bg='#FFDAB9')
        cardNumberLabel.grid(row=5, column=0, sticky='ne')
        cardNumberLabel['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')
        self.cardNumberEntry = tkinter.Entry(self.f3)
        CardN = GenerateRandomInfo.getCardNumber()
        self.cardNumberEntry.insert(0, CardN)
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
    def WarningWindow(self):

        self.window = tkinter.Tk()
        self.window.title("PARKING LOT")
        self.window.geometry("200x100-200-400")
        self.window.config(bg="#FA8072")
        self.window['pady'] = 5

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
        # ok['pady'] = 5

        self.window.minsize(200, 100)
        self.window.maxsize(200, 100)
        self.window.mainloop()

    # check methode for checking all information of car
    def CheckInfo(self):
        if self.carColorEntry.get() and self.carTypeEntry.get() and self.carNumberEntry.get() and self.cardTypeEntry.get() and self.cardNumberEntry.get():
            self.info()
            return self.ParkingTicket()
        else:
            return self.WarningWindow()

    # methode for assigned all info
    def info(self):
        self.carNumber = self.carNumberEntry.get()
        self.carType = self.carTypeEntry.get()
        self.carColor = self.carColorEntry.get()
        self.__cardType = self.cardTypeEntry.get()
        self.__cardNumber = self.cardNumberEntry.get()

    # methode for show user parking ticket
    def ParkingTicket(self):

        now = datetime.now()
        self.data = date.today()
        self.timeNow = now.strftime('%I:%M %p')

        arr1 = ['\tCar Number', '\tCar Type', '\tCar Color', '\tParking Date', '\tParking Time']
        arr2 = [self.carNumber, self.carType, self.carColor, date.today(), now.strftime('%I:%M %p')]

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

        backButton = tkinter.Button(self.f4, text='Back', bg='#FF7F50', activebackground='#FFA500',
                                    command=self.f4.destroy)
        backButton.grid(row=2, column=2, sticky='en')
        # print button on f4 frame
        getTicketButton = tkinter.Button(self.f4, text='Get Ticket', bg='#FF7F50', activebackground='#FFA500',
                                     command=self.sendInfoToMail)
        getTicketButton.grid(row=2, column=1, sticky='nw')

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

    def sendInfoToMail(self):
        # parking ticket
        str = f"""
        __________________________________________
        
         \t\tCar Number : {self.carNumber}
         \t\tCar Type : {self.carType}
         \t\tCar Color : {self.carColor}
         \t\tDate : {self.data}
         \t\tParking Time : {self.timeNow}
        _________________________________________"""

        # object of sendEmail class
        obj = SendEmail.sendParkingTicket(str)
        obj.windowForEmail()

    # Store Information in Data base
    def storeInfoInDB(self):
        pass
