from random import *
import string
import mysql.connector
import random

mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='Kiran@982326',
    database='ParkingLot'
)


# car number
state = ['MH', 'BR', 'HR', 'KA', 'MP', 'ML', 'PB', 'DL', 'UP', 'UT', 'TN', 'RJ', 'KL', 'TG']
districts = ['02', '27', '31', '20', '35', '40', '45', '15', '19']
alphabet = ['AB', 'PO', 'RT', 'AQ', 'QN', 'KS', 'TY', 'AK', 'SU', 'VR']

# car type
carType = ["SEDAN", "VAN", "MINIVAN", "BUS", "PICKUP-TRUCK", "HATCHBACK"]

# car color
carColor = ['RED', 'YELLOW', 'WHITE', 'BLACK', 'VIOLET', 'BLUE', 'PINK', 'GREEN', 'BROWN', 'ORANGE']

# card type
card = ["DEBIT", "CREDIT"]


# generate car number
def CarNumberRand():
    CarNum = ''
    CarNum = choice(state)+" "+choice(districts)+" "+choice(alphabet)

    chars = string.digits
    num = ''.join(choice(chars) for _ in range(4))
    CarNum = CarNum+" "+num
    return CarNum


# generate car color
def CarColorRand():
    Color = choice(carColor)
    return Color


# generate car type
def CarTypeRand():
    Type = choice(carType)
    return Type


# generate card type
def __CardTypeRand():
    __CardType = choice(card)
    return __CardType


# generate card number
def __CardNumberRand():
    __CardNum = ''
    for i in range(16):
        __CardNum = __CardNum + str(randint(0, 9))
    return __CardNum


def getCardType():
    return __CardTypeRand()


def getCardNumber():
    return __CardNumberRand()


def getSpotNumDB():
    mycursor = mydb.cursor()

    sql = "SELECT SrNum FROM ParkingLot.ParkingSpot WHERE Spot = 'Null'"

    mycursor.execute(sql)
    li = []
    for i in mycursor:
        li.append(list(i)[0])

    if len(li) == 0:
        return None

    # print(li)
    mydb.commit()
    return random.choice(li)

