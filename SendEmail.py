import smtplib
import tkinter
from tkinter import font


class sendParkingTicket(object):

    def __init__(self, str):
        self.str = str
        self.receiverEmail = None

    def windowForEmail(self):

        self.messageWindow = tkinter.Tk()

        self.messageWindow.title("Parking Lot")
        self.messageWindow.geometry("200x100-200-400")
        self.messageWindow.config(bg="#FA8072")
        self.messageWindow['pady'] = 5
        label = tkinter.Label(self.messageWindow, text='Enter your Email address', bg='#FA8072')
        label['font'] = tkinter.font.Font(size=20, family='Helvetica', weight='bold')
        label.pack()

        self.mailAddress = tkinter.Entry(self.messageWindow, width=25)
        self.mailAddress.pack()

        sendButton = tkinter.Button(self.messageWindow, text='Send', bg='#FF7F50', activebackground='#FFA500',
                                    command=self.send_Email)
        sendButton.pack(side='bottom', anchor='s')

        self.messageWindow.minsize(250, 100)
        self.messageWindow.maxsize(250, 100)
        self.messageWindow.mainloop()

    def send_Email(self):

        self.receiverEmail = self.mailAddress.get()
        try:
            ob = smtplib.SMTP('imap.gmail.com', 587)
            ob.starttls()
            ob.login("MailID@gmail.com", "passward")
            subject = "PARKING TICKET"

            body = self.str
            message = 'Subject : {}\n\n{}'.format(subject, body)
            ob.sendmail("ParkingLotSystem12@gmail.com", self.receiverEmail, message)
            # print("send successful..")
            ob.quit()

            self.messageWindow.destroy()

            self.window = tkinter.Tk()
            self.window.title("Parking Lot")
            self.window.geometry("200x70-200-400")
            self.window.config(bg="#FA8072")
            self.window['pady'] = 20

            label = tkinter.Label(self.window, text='Email Sent Successfully!', bg="#FA8072")
            label.pack()

            self.window.minsize(200, 70)
            self.window.maxsize(200, 70)

            self.window.after(2500, self.window.destroy)

            self.window.mainloop()

        except smtplib.SMTPRecipientsRefused as e:
            self.messageWindow.destroy()
            self.warning = tkinter.Tk()
            self.warning.title("Parking Lot")
            self.warning.geometry("200x70-250-400")
            self.warning.config(bg="#FA8072")
            self.warning["pady"] = 15

            label = tkinter.Label(self.warning, text="Please enter correct Email!", bg="#FA8072")
            label.pack()

            self.warning.minsize(200, 70)
            self.warning.maxsize(200, 70)

            self.warning.after(2500, self.warning.destroy)

            self.warning.mainloop()
