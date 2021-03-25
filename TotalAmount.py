def TotalAmount(PaTime, PaDate, ExTime, ExDate):
    ExDate = str(ExDate)
    PaDate = str(PaDate)
    firstDay = int(PaDate[8:10])
    lastDay = int(ExDate[8:10])
    firstMonth = int(PaDate[5:7])
    lastMonth = int(ExDate[5:7])
    firstYear = int(PaDate[0:4])

    if firstMonth != lastMonth:
        daysInMonth = 0
        li = [1, 3, 5, 7, 8, 10, 12]
        if firstMonth in li:
            daysInMonth = 31
        else:
            if firstMonth == 2:
                if firstYear % 4 == 0:
                    daysInMonth = 29
                else:
                    daysInMonth = 28
            else:
                daysInMonth = 30

        Days = daysInMonth - firstDay
        Days = Days + (lastDay - 1)
        HourInTotalDays = Days * 24

        # Total hour in 1st day
        HoursInFirstDay = 0
        MinutesInFirstDay = 0

        if PaTime[6:8] == 'AM':
            if int(PaTime[:2]) == 12:
                HoursInFirstDay = 11 + 12
                MinutesInFirstDay = 60 - int(PaTime[3:5])
            else:
                HoursInFirstDay = (12 - (int(PaTime[:2]) + 1)) + 12
                MinutesInFirstDay = 60 - int(PaTime[3:5])
        elif PaTime[6:8] == 'PM':
            if int(PaTime[:2]) == 12:
                HoursInFirstDay = 11
                MinutesInFirstDay = 60 - int(PaTime[3:5])
            else:
                HoursInFirstDay = (12 - (int(PaTime[:2]) + 1))
                MinutesInFirstDay = 60 - int(PaTime[3:5])

        # Total hour and minute in last day
        HoursInLastDay = 0
        MinutesInLastDay = 0

        if ExTime[6:8] == 'AM':
            if int(ExTime[:2]) == 12:
                HoursInLastDay = 0
                MinutesInLastDay = int(ExTime[3:5])
            else:
                HoursInLastDay = int(ExTime[:2])
                MinutesInLastDay = int(ExTime[3:5])
        elif ExTime[6:8] == 'PM':
            if int(ExTime[:2]) == 12:
                HoursInLastDay = 12
                MinutesInLastDay = int(ExTime[3:5])
            else:
                HoursInLastDay = 12 + int(ExTime[:2])
                MinutesInLastDay = int(ExTime[3:5])

        # Total hour and minute
        hour = HourInTotalDays + HoursInFirstDay + HoursInLastDay
        minute = MinutesInFirstDay + MinutesInLastDay

        if minute >= 60:
            minute = minute - 60
            hour += 1

        return AmountCal(hour, minute)

    # Time calculation for same month
    else:
        if lastDay - firstDay >= 2:
            Days = (lastDay - (firstDay - 1)) - 2
            HourInTotalDays = Days * 24

            # Total hour in 1st day
            HoursInFirstDay = 0
            MinutesInFirstDay = 0

            if PaTime[6:8] == 'AM':
                if int(PaTime[:2]) == 12:
                    HoursInFirstDay = 11 + 12
                    MinutesInFirstDay = 60 - int(PaTime[3:5])
                else:
                    HoursInFirstDay = (12 - (int(PaTime[:2]) + 1)) + 12
                    MinutesInFirstDay = 60 - int(PaTime[3:5])
            elif PaTime[6:8] == 'PM':
                if int(PaTime[:2]) == 12:
                    HoursInFirstDay = 11
                    MinutesInFirstDay = 60 - int(PaTime[3:5])
                else:
                    HoursInFirstDay = (12 - (int(PaTime[:2]) + 1))
                    MinutesInFirstDay = 60 - int(PaTime[3:5])

            # Total hour and minute in last day
            HoursInLastDay = 0
            MinutesInLastDay = 0

            if ExTime[6:8] == 'AM':
                if int(ExTime[:2]) == 12:
                    HoursInLastDay = 0
                    MinutesInLastDay = int(ExTime[3:5])
                else:
                    HoursInLastDay = int(ExTime[:2])
                    MinutesInLastDay = int(ExTime[3:5])
            elif ExTime[6:8] == 'PM':
                if int(ExTime[:2]) == 12:
                    HoursInLastDay = 12
                    MinutesInLastDay = int(ExTime[3:5])
                else:
                    HoursInLastDay = 12 + int(ExTime[:2])
                    MinutesInLastDay = int(ExTime[3:5])

            # Total hour and minute
            hour = HourInTotalDays + HoursInFirstDay + HoursInLastDay
            minute = MinutesInFirstDay + MinutesInLastDay

            if minute >= 60:
                minute = minute - 60
                hour += 1

            return AmountCal(hour, minute)

        # for one day difference only
        elif lastDay - firstDay == 1:
            # Total hour in 1st day
            HoursInFirstDay = 0
            MinutesInFirstDay = 0

            if PaTime[6:8] == 'AM':
                if int(PaTime[:2]) == 12:
                    HoursInFirstDay = 11 + 12
                    MinutesInFirstDay = 60 - int(PaTime[3:5])
                else:
                    HoursInFirstDay = (12 - (int(PaTime[:2]) + 1)) + 12
                    MinutesInFirstDay = 60 - int(PaTime[3:5])
            elif PaTime[6:8] == 'PM':
                if int(PaTime[:2]) == 12:
                    HoursInFirstDay = 11
                    MinutesInFirstDay = 60 - int(PaTime[3:5])
                else:
                    HoursInFirstDay = (12 - (int(PaTime[:2]) + 1))
                    MinutesInFirstDay = 60 - int(PaTime[3:5])

            # Total hour and minute in last day
            HoursInLastDay = 0
            MinutesInLastDay = 0

            if ExTime[6:8] == 'AM':
                if int(ExTime[:2]) == 12:
                    HoursInLastDay = 0
                    MinutesInLastDay = int(ExTime[3:5])
                else:
                    HoursInLastDay = int(ExTime[:2])
                    MinutesInLastDay = int(ExTime[3:5])
            elif ExTime[6:8] == 'PM':
                if int(ExTime[:2]) == 12:
                    HoursInLastDay = 12
                    MinutesInLastDay = int(ExTime[3:5])
                else:
                    HoursInLastDay = 12 + int(ExTime[:2])
                    MinutesInLastDay = int(ExTime[3:5])

            # Total hour and minute
            hour = HoursInFirstDay + HoursInLastDay
            minute = MinutesInFirstDay + MinutesInLastDay

            if minute >= 60:
                minute = minute - 60
                hour += 1

            return AmountCal(hour, minute)

        # for one single day
        elif lastDay - firstDay == 0:
            parkedHour = 0; parkedMinute = 0; ExitHour = 0; ExitMinute = 0
            hour = 0
            minute = 0

            if PaTime[6:8] == 'AM' and ExTime[6:8] == 'AM':
                if int(PaTime[:2]) == 12:
                    hour = int(ExTime[:2])
                    minute = (60 - int(PaTime[3:5])) + int(ExTime[3:5])
                else:
                    hour = int(ExTime[:2]) - (int(PaTime[:2]) + 1)
                    minute = (60 - int(PaTime[3:5])) + int(ExTime[3:5])

            elif PaTime[6:8] == 'PM' and ExTime[6:8] == 'PM':
                if int(PaTime[:2]) == 12:
                    hour = int(ExTime[:2])
                    minute = (60 - int(PaTime[3:5])) + int(ExTime[3:5])
                else:
                    hour = int(ExTime[:2]) - (int(PaTime[:2]) + 1)
                    minute = (60 - int(PaTime[3:5])) + int(ExTime[3:5])

            elif PaTime[6:8] == 'AM' and ExTime[6:8] == 'Pm':
                if int(PaTime[:2]) == 12:
                    parkedHour = 12
                    parkedMinute = 60 - int(PaTime[3:5])
                else:
                    parkedHour = 12 - (int(PaTime[:2]) + 1)
                    parkedMinute = 60 - int(PaTime[3:5])

                if int(ExTime[:2]) == 12:
                    ExitHour = 0
                    ExitMinute = 60 - int(ExTime[3:5])
                else:
                    ExitHour = int(ExTime[:2])
                    ExitMinute = int(ExTime[3:5])

                hour = parkedHour + ExitHour
                minute = parkedMinute + ExitMinute

            if minute >= 60:
                minute = minute - 60
                hour = hour + 1

            return AmountCal(hour, minute)


def AmountCal(hour, minute):
    HourAmount = 30
    TotalAmountForHour = hour * HourAmount
    TotalAmountForMinute = 0
    if (minute < 60) and (minute >= 30):
        TotalAmountForMinute = 20
    elif (minute < 30) and (minute >= 15):
        TotalAmountForMinute = 15
    elif (minute < 15) and (minute >= 1):
        TotalAmountForMinute = 10

    amount = TotalAmountForHour + TotalAmountForMinute
    return amount
