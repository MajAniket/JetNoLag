from guizero import *
from datetime import *
import datetime

times = ["GMT -12", "GMT -11", "GMT -10", "GMT -9", "GMT -8", "GMT -7", "GMT -6", "GMT -5", "GMT -4", "GMT -3", "GMT -2", "GMT -1","GMT +0", "GMT +1", "GMT +2", "GMT +3", "GMT +4", "GMT +5", "GMT +6", "GMT +7", "GMT +8", "GMT +9", "GMT +10", "GMT +11", "GMT +12"]

app = App(title = "Jet No Lag", width = "1200", height = "700", bg = "#D8E0FF")

def submit():
    CZ = currentZone.value
    DZ = destinationZone.value
    cz = int(times.index(CZ))
    dz = int(times.index(DZ))
    timeDifference = (dz - 12) - (cz -12)
    
    
    a = datetime.datetime(int(year.value), int(month.value), int(day.value))
    dateDifference = a.date() - date.today()
    daysDate = dateDifference.days
    change = int(timeDifference) / int(daysDate)*60 #this is calculating how much time needs to be increased or decreased by in minutes each day
    
    t = datetime(hours = int(sliderHour.value), minutes = int(sliderMinutes.value)) #formating the time the user input into datetime
    text.show()
    for i in range(daysDate): #works out the time each day and adds it to the box
        newTime = t + timedelta(minutes = change)
        output.value += "Day", str(i), ": ", str(newTime), "\n"
        t = newTime
    

name = Text(app, text = "Jet No Lag", size = 50, align = "top", color = "#000000")

description = Text(app,
                   text = "No one likes jetlag. Input information about your trip and get a custom sleep schedule to \n follow before your departure to transition smoothly into your new time zone."
                   , size = 20 , color = "#000000")


questions = Box(app, layout = "grid")

#time zone information
currentZoneText = Text(questions, text = "\nPick your current locations time zone", grid = [0,2])

currentZone = Combo(questions,
                   options = ["GMT -12", "GMT -11", "GMT -10", "GMT -9", "GMT -8", "GMT -7", "GMT -6", "GMT -5", "GMT -4", "GMT -3", "GMT -2", "GMT -1",
                              "GMT +0", "GMT +1", "GMT +2", "GMT +3", "GMT +4", "GMT +5", "GMT +6", "GMT +7", "GMT +8", "GMT +9", "GMT +10", "GMT +11", "GMT +12"],
                   selected = "GMT", width = 20, grid = [0,4])
currentZone.bg = "white"

destinationZoneText = Text(questions, text = "\nPick your destination locations time zone", grid = [0,6])

destinationZone = Combo(questions,
                   options = ["GMT -12", "GMT -11", "GMT -10", "GMT -9", "GMT -8", "GMT -7", "GMT -6", "GMT -5", "GMT -4", "GMT -3", "GMT -2", "GMT -1",
                              "GMT +0", "GMT +1", "GMT +2", "GMT +3", "GMT +4", "GMT +5", "GMT +6", "GMT +7", "GMT +8", "GMT +9", "GMT +10", "GMT +11", "GMT +12"],
                   selected = "GMT", width = 20, grid = [0,8])
destinationZone.bg = "white"

#trip date information
tripdate = Text(questions, text = "\nDate of Trip", grid = [6,2], )

day = Combo(questions,
            options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14","15",
                       "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29","30", "31"],
            selected = "1", width = 10, grid = [6,4])
day.bg = "white"

month = Combo(questions,
            options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            selected = "1", width = 10, grid = [6,5])
month.bg = "white"

year = TextBox(questions, text = "2021", width = "20", height = "87", grid = [6,6])
year.bg = "white"

wakeup = Text(questions, text = "\nUsual Wakeup Time", grid = [6,8])
sliderHour = Slider(questions, start = "0", end = "23", grid = [6,9])
sliderMinutes = Slider(questions, start = "0", end = "59", grid = [6, 10])

submit_btn = PushButton(questions, text = "Submit", command = submit, grid = [7, 12])
submit_btn.bg = "green"
submit_btn.color = "white"

text = Text(questions, text = "Sleep Schedule", grid = [9,2]).hide()
output = Text(questions, text = "", grid = [9,3])

output.bg = "#808080"


app.display()


