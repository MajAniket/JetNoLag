from guizero import *
from datetime import *
import datetime

times = ["GMT -12", "GMT -11", "GMT -10", "GMT -9", "GMT -8", "GMT -7", "GMT -6", "GMT -5", "GMT -4", "GMT -3", "GMT -2", "GMT -1","GMT +0", "GMT +1", "GMT +2", "GMT +3", "GMT +4", "GMT +5", "GMT +6", "GMT +7", "GMT +8", "GMT +9", "GMT +10", "GMT +11", "GMT +12"]

app = App(title = "Jet No Lag", width = "1200", height = "700", bg = "#D8E0FF")

def submit():
    CZ = currentZone.value
    DZ = destintionZone.value
    cz = times.index(CZ)
    dz = times.index(DZ)
    timeDifference = (dz - 12) - (cz -12)
    
    today = date.today()
    a = datetime.datetime(dateText.value[3], dateText.value[5,6], dateText.value[8,9])
    b = datetime.datetime(today[3], today[5,6], today[8,9])
    dateDifference = a-b
    
    change = int(timeDifference / dateDifference)*60
    t = datetime(hours = wakeText.value[1], minutes = wakeText.value[3,4])
    for i in range(dateDifference):
        newTime = t + timedelta(minutes = change)
        output.value += "Day", str(i), ": ", str(newTime), "\n"
        t = newTime
    

name = Text(app, text = "Jet No Lag", size = 50, align = "top", color = "#000000")

description = Text(app,
                   text = "No one likes jetlag. Input information about your trip and get a custom sleep schedule to \n follow before your departure to transition smoothly into your new time zone."
                   , size = 20 , color = "#000000")


questions = Box(app)

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

tripdate = Text(questions, text = "\nDate of Trip")
dateText = TextBox(questions, text = "2021-07-04", width = "30", height = "87")

wakeup = Text(questions, text = "\nUsual Wakeup Time")
wakeText = TextBox(questions, text = "06: 00", width = "30", height = "87") #, color = "#808080"

submit_btn = PushButton(app, text = "Submit", command = submit)

sleepbox = Box(app)
text = Text(sleepbox, text = "Sleep Schedule")
output = Text(sleepbox, text = "")

timetable = Box(sleepbox)
timetable.bg = "#808080"


app.display()


