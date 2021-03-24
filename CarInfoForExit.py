import tkinter
from tkinter import font
import mysql.connector
from datetime import date, datetime
import TotalAmount
mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='Kiran@982326',
    database='ParkingLot'
)


# class for getting information for exit user car
class ExitCarInfo(object):

    def __init__(self):
        self.PaDate = None
        self.PaTime = None
        self.ExDate = None
        self.ExTime = None
        self.carNumber = None
        self.carType = None
        self.carColor = None
        self.cardNumber = None
        self.cardType = None
        self.SpotNum = None
        self.TotalAmount = None

    def ExitCar(self):

        # frame for getting car number of user
        self.f2 = tkinter.Frame()
        self.f2.place(x=0, y=0, width=640, height=480)
        self.f2.config(bg='#FA8072')

        LabelEx = tkinter.Label(self.f2, text='  Enter your car number : ', bg='#FFDAB9')
        LabelEx.grid(row=0, column=0, sticky='s')

        self.CarNumberEntry = tkinter.Entry(self.f2)
        self.CarNumberEntry.grid(row=0, column=1, sticky='s')

        # ok button
        ok = tkinter.Button(self.f2, text='Ok', bg='#FF7F50', activebackground='#FFA500', command=self.TotalTime)
        ok.grid(row=2, column=1, sticky='e')

        # cancel button for destroy frame self.f2
        cancel = tkinter.Button(self.f2, text='Cancel', bg='#FF7F50', activebackground='#FFA500', command=self.f2.destroy)
        cancel.grid(row=2, column=2, sticky='w')

        # configure the row of frame self.f2
        self.f2.rowconfigure(0, weight=1)
        self.f2.rowconfigure(1, weight=1)
        self.f2.rowconfigure(2, weight=1)

        # configure the column of frame self.f2
        self.f2.columnconfigure(0, weight=1)
        self.f2.columnconfigure(1, weight=1)
        self.f2.columnconfigure(2, weight=1)

    def TotalTime(self):
        mycursor = mydb.cursor()
        carNum = str(self.CarNumberEntry.get())
        sql = "SELECT CarNumber, CarColor, carType, CardType, CardNumber, ParkingTime, ParkingDate, SpotNum FROM ParkingLot.ParkingInfo WHERE CarNumber = %s"
        val = [carNum]

        mycursor.execute(sql, val)

        for i in mycursor:
            self.carNumber = str(i[0])
            self.carColor = str(i[1])
            self.carType = str(i[2])
            self.cardType = str(i[3])
            self.cardNumber = str(i[4])
            self.PaTime = str(i[5])
            self.PaDate = str(i[6])
            self.SpotNum = i[7]

        self.DeleteDataAndTicket()

    def DeleteDataAndTicket(self):
        self.DeleteDataDB()
        self.TicketFrame()

    def TicketFrame(self):
        now = datetime.now()
        self.ExDate = date.today()
        self.ExTime = str(now.strftime('%I:%M %p'))
        self.TotalAmount = TotalAmount.TotalAmount(self.PaTime, self.PaDate, self.ExTime, self.ExDate)

        arr1 = ['\tCar Number', '\tCar Type', '\tCar Color', '\tParking Date', '\tParking Time', '\tSpot Number', '\tExit Date', '\tExit Time', '\tTotal Amount']
        arr2 = [self.carNumber, self.carType, self.carColor, self.PaDate, self.PaTime, self.SpotNum, self.ExTime, self.ExDate, self.TotalAmount]

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
        la.place(x=160, y=90, width=330, height=290)
        la.config(bg='#90EE90')
        la['padx'] = 8

        # show all information on parking ticket
        for i in range(9):
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
        for i in range(9):
            la.rowconfigure(i, weight=1)

        # configure the column of frame la
        la.columnconfigure(0, weight=1)
        la.columnconfigure(1, weight=1)
        la.columnconfigure(2, weight=3)

        # ok button on f4 frame
        okButton = tkinter.Button(self.f4, text='  Ok  ', bg='#FF7F50', activebackground='#FFA500',
                                  command=self.Des)
        okButton.grid(row=2, column=1, sticky='ne')

        # configure the row of frame f4
        self.f4.rowconfigure(0, weight=1)
        self.f4.rowconfigure(1, weight=5)
        self.f4.rowconfigure(2, weight=1)

        # configure the column of frame f4
        self.f4.columnconfigure(0, weight=1)
        self.f4.columnconfigure(1, weight=2)
        self.f4.columnconfigure(2, weight=1)

    def Des(self):
        self.f4.destroy()
        self.f2.destroy()

    def DeleteDataDB(self):
        mycursor = mydb.cursor()
        sql = "DELETE FROM ParkingLot.ParkingInfo WHERE CarNumber = %s"
        val = [self.carNumber]
        mycursor.execute(sql, val)

        sql = "UPDATE ParkingLot.ParkingSpot SET Spot = 'Null' WHERE SrNum = %s"
        val = [self.SpotNum]
        mycursor.execute(sql, val)

        mydb.commit()
