from guizero import *
from datetime import *
import datetime

times = ["GMT -12", "GMT -11", "GMT -10", "GMT -9", "GMT -8", "GMT -7", "GMT -6", "GMT -5", "GMT -4", "GMT -3", "GMT -2", "GMT -1","GMT +0", "GMT +1", "GMT +2", "GMT +3", "GMT +4", "GMT +5", "GMT +6", "GMT +7", "GMT +8", "GMT +9", "GMT +10", "GMT +11", "GMT +12"]

app = App(title = "Jet No Lag", width = "1200", height = "700", bg = "#D8E0FF")

def submit():
    CZ = currentZone.value
    DZ = destintionZone.value
    cz = int(times.index(CZ))
    dz = int(times.index(DZ))
    timeDifference = (dz - 12) - (cz -12)
    
    
    a = datetime.datetime(int(year.value), int(month.value), int(day.value))
    dateDifference = a.date() - date.today()
    daysDate = dateDifference.days
    change = int(timeDifference) / int(daysDate)*60 #this is calculating how much time needs to be increased or decreased by in minutes each day
    
    t = datetime(hours = int(wakeText.value[1]), minutes = int(wakeText.value[3,4])) #formating the time the user input into datetime
    
    for i in range(dateDifference): #works out the time each day and adds it to the box
        newTime = t + timedelta(minutes = change)
        output.value += "Day", str(i), ": ", str(newTime), "\n"
        t = newTime
    

name = Text(app, text = "Jet No Lag", size = 50, align = "top", color = "#000000")

description = Text(app,
                   text = "No one likes jetlag. Input information about your trip and get a custom sleep schedule to \n follow before your departure to transition smoothly into your new time zone."
                   , size = 20 , color = "#000000")


questions = Box(app)

#time zone information
currentZoneText = Text(questions, text = "\nPick your current locations time zone")

currentZone = Combo(questions,
                   options = ["GMT -12", "GMT -11", "GMT -10", "GMT -9", "GMT -8", "GMT -7", "GMT -6", "GMT -5", "GMT -4", "GMT -3", "GMT -2", "GMT -1",
                              "GMT +0", "GMT +1", "GMT +2", "GMT +3", "GMT +4", "GMT +5", "GMT +6", "GMT +7", "GMT +8", "GMT +9", "GMT +10", "GMT +11", "GMT +12"],
                   selected = "GMT", width = 20)

destinationZoneText = Text(questions, text = "\nPick your destination locations time zone")

destintionZone = Combo(questions,
                   options = ["GMT -12", "GMT -11", "GMT -10", "GMT -9", "GMT -8", "GMT -7", "GMT -6", "GMT -5", "GMT -4", "GMT -3", "GMT -2", "GMT -1",
                              "GMT +0", "GMT +1", "GMT +2", "GMT +3", "GMT +4", "GMT +5", "GMT +6", "GMT +7", "GMT +8", "GMT +9", "GMT +10", "GMT +11", "GMT +12"],
                   selected = "GMT", width = 20)

#trip date information
tripdate = Text(questions, text = "\nDate of Trip")
day = Combo(questions,
            options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14","15",
                       "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29","30", "31"],
            selected = "1", width = 10)

month = Combo(questions,
            options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            selected = "1", width = 10)

year = TextBox(questions, text = "2021", width = "30", height = "87")

wakeup = Text(questions, text = "\nUsual Wakeup Time")
wakeText = TextBox(questions, text = "06: 00", width = "30", height = "87")

submit_btn = PushButton(app, text = "Submit", command = submit)

sleepbox = Box(app)
text = Text(sleepbox, text = "Sleep Schedule")
output = Text(sleepbox, text = "")

timetable = Box(sleepbox)
timetable.bg = "#808080"


app.display()


