from tkinter import *
import time
import datetime
import winsound

def alarm(set_time, set_date):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        sptime = current_time.strftime("%H:%M:%S") #time specified by the user
        spdate = current_time.strftime("%d/%m/%Y") #date specified by the user
        print("The date and the time is : {} {}".format(sptime,spdate))
        if set_time == sptime and set_date == spdate:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def set_alarm():
    set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    set_date = f"{day.get()}/{month.get()}/{year.get()}"
    alarm(set_time, set_date)

if __name__ == "__main__":
    clock = Tk()

    clock.title("Alarm Clock")
    clock.geometry("400x200")
    time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
    addTime = Label(clock,text = "Hour  Min   Sec   Day   Month  Year",font=60).place(x = 110)
    setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

    # The Variables we require to set the alarm(initialization):
    hour = StringVar()
    min = StringVar()
    sec = StringVar()
    day = StringVar()
    month = StringVar()
    year = StringVar()

    #Time required to set the alarm clock:
    hourTime = Entry(clock, textvariable=hour, bg="pink",width = 15).place(x=110,y=30)
    minTime = Entry(clock, textvariable=min, bg="pink",width = 15).place(x=150,y=30)
    secTime = Entry(clock, textvariable=sec, bg="pink",width = 15).place(x=200,y=30)
    dayTime = Entry(clock, textvariable=day, bg="pink",width = 15).place(x=230,y=30)
    monTime = Entry(clock, textvariable=month, bg="pink",width = 15).place(x=270,y=30)
    yearTime = Entry(clock, textvariable=year, bg="pink",width = 15).place(x=300,y=30)
    #To take the time input by user:
    submit = Button(clock,text="Set Alarm",fg="red",width = 10,command = set_alarm).place(x =110,y=70)
    clock.mainloop()
