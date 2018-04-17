__author__ = 'Razvan Bouros'
from graphics import *
from math import *
import datetime



def drawSystemClock(mode):
    uren = datetime.datetime.now().time().hour
    minuten = datetime.datetime.now().time().minute
    win = GraphicsWindow(300, 300)
    canvas = win.canvas()

    # Calculations for each of the watch hands
    minutenwijzer = (90 - minuten * 6) * pi / 180.0
    uurwijzer = (90 - (uren + minuten / 60) * 30) * pi / 180

    # Drawing on the canvas that was chosen earlier.
    canvas.setOutline("black")
    canvas.drawRect(50, 10, 200, 230)
    canvas.drawOval(75, 25, 150, 150)
    canvas.setTextFont(None, 14, None)

    # Drawing of the text under the clock: digital clock 24h or 12h
    if mode == 12:
        if uren > 12:
            uren = uren - 12
            Digitaalklok = str(round(uren)) + ":" + str(round(minuten)).zfill(2), "pm"
        elif uren <= 12:
            Digitaalklok = str(round(uren)) + ":" + str(round(minuten)).zfill(2), "am"
    elif mode == 24:
        if uren > 12:
            Digitaalklok = str(round(uren)) + ":" + str(round(minuten)).zfill(2)
        Digitaalklok = str(round(uren)) + ":" + str(round(minuten)).zfill(2)

    canvas.drawText(120, 195, Digitaalklok)
    canvas.setTextFont(None, 14, None)

    # calculating end coordinates for minute and hour hand.
    x2m = (150 + 75 * cos(minutenwijzer))
    y2m = (100 - 75 * sin(minutenwijzer))
    x2h = (150 + 50 * cos(uurwijzer))
    y2h = (100 - 50 * sin(uurwijzer))

    # drawing clock hands with the above calculated coordinates as end coordinates.
    canvas.drawLine(150, 100, x2m, y2m)
    canvas.drawLine(150, 100, x2h, y2h)

    win.wait()
def drawChosenClock(mode,uren,minuten):
    win = GraphicsWindow(300, 300)
    canvas = win.canvas()

    # Calculations for each of the watch hands
    minutenwijzer = (90 - minuten * 6) * pi / 180.0
    uurwijzer = (90 - (uren + minuten / 60) * 30) * pi / 180

    # Drawing on the canvas that was chosen earlier.
    canvas.setOutline("black")
    canvas.drawRect(50, 10, 200, 230)
    canvas.drawOval(75, 25, 150, 150)
    canvas.setTextFont(None, 14, None)

    # Drawing of the text under the clock: digital clock 24h or 12h
    if mode == 12:
        if uren > 12:
            uren = uren - 12
            Digitaalklok = str(round(uren)) + ":" + str(round(minuten)).zfill(2), "pm"
        elif uren <= 12:
            Digitaalklok = str(round(uren)) + ":" + str(round(minuten)).zfill(2), "am"
    elif mode == 24:
        if uren > 12:
            Digitaalklok = str(round(uren)) + ":" + str(round(minuten)).zfill(2)
        Digitaalklok = str(round(uren)) + ":" + str(round(minuten)).zfill(2)

    canvas.drawText(120, 195, Digitaalklok)
    canvas.setTextFont(None, 14, None)

    # calculating end coordinates for minute and hour hand.
    x2m = (150 + 75 * cos(minutenwijzer))
    y2m = (100 - 75 * sin(minutenwijzer))
    x2h = (150 + 50 * cos(uurwijzer))
    y2h = (100 - 50 * sin(uurwijzer))

    # drawing clock hands with the above calculated coordinates as end coordinates.
    canvas.drawLine(150, 100, x2m, y2m)
    canvas.drawLine(150, 100, x2h, y2h)

    win.wait()
def chooseFormat():
    format = input("24h of 12h format for display on clock, Type in 12 or 24 for the respective formats? ")
    if format.isnumeric() == True:
        if format == "12":
            return 12
        elif format == "24":
            return 24
        else:
            print("Wrong Input numeric!")
            return 0
    else:
        print("Wrong Input alphanumeric!")
        return 0
def chooseTime():
    #choice for systemtime or own time choice
    inputtedTime = input(" (1) voor System time, (2) Zelf een tijd bepalen ")
    if inputtedTime.isnumeric() == False:
        print("Wrong input alphanumeric!")
        #print(systemtime)
        return 0
    elif inputtedTime.isnumeric() == True and inputtedTime == "1":
        #print(systemtime)
        return 1
    elif inputtedTime.isnumeric() == True and inputtedTime == "2":
        #print(systemtime)
        return 2
    else:
        return 0
def inputTime():
    #time = input("Type in the desired time 'HH:MM' :")
    uren = input("How many hours ? '0-23' ")
    minuten = input("How many minutes ? '0-59'")

#If the HH:MM version of the code is need it's in working version here, just unhash the #time and the minuten/uren and it works.
    #but hash the other version of the declaration
    #minuten = time[-2:]
    #uren = time[:2]
    # else:
    if uren.isnumeric()==False or minuten.isnumeric()==False:
        print("Wrong input!")
        inputTime()
    elif int(uren) <= 23 and int(minuten) <= 59:
                return int(uren), int(minuten)
def main():
   chosentime=chooseTime()
   mode=chooseFormat()

#Here the functions are handled to create the complete product
   if chosentime== 1 and mode== 12:
        mode=12
        drawSystemClock(mode)
   elif chosentime==1 and mode==24:
        mode =24
        drawSystemClock(mode)
   elif chosentime==2 and mode==12:
       uren, minuten = inputTime()
       mode = 12
       drawChosenClock(mode, uren, minuten)
   elif chosentime==2 and mode==24:
       uren, minuten = inputTime()
       mode = 24
       drawChosenClock(mode, uren, minuten)
   else:
        print("Verkeerde input! Begin maar opnieuw!")
        main()

main()
