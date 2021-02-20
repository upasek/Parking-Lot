import tkinter


# class for getting information for exit user car
class ExitCarInfo(object):

    def ExitCar(self):

        # frame for getting car number of user
        f2 = tkinter.Frame()
        f2.place(x=0, y=0, width=640, height=480)
        f2.config(bg='#FA8072')

        LabelEx = tkinter.Label(f2, text='  Enter your car number : ', bg='#FFDAB9')
        LabelEx.grid(row=0, column=0, sticky='s')

        CarNumberEntry = tkinter.Entry(f2)
        CarNumberEntry.grid(row=0, column=1, sticky='s')

        # ok button
        ok = tkinter.Button(f2, text='Ok', bg='#FF7F50', activebackground='#FFA500')
        ok.grid(row=2, column=1, sticky='e')

        # cancel button for destroy frame f2
        cancel = tkinter.Button(f2, text='Cancel', bg='#FF7F50', activebackground='#FFA500', command=f2.destroy)
        cancel.grid(row=2, column=2, sticky='w')

        # configure the row of frame f2
        f2.rowconfigure(0, weight=1)
        f2.rowconfigure(1, weight=1)
        f2.rowconfigure(2, weight=1)

        # configure the column of frame f2
        f2.columnconfigure(0, weight=1)
        f2.columnconfigure(1, weight=1)
        f2.columnconfigure(2, weight=1)