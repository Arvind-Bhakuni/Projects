import datetime as dt
from tkinter import *
import time
import winsound

def alarm_clock(set_timer):
	while True:
		time.sleep(2)
		present_time = dt.datetime.now().strftime("%H:%M:%S")
		present_date = dt.datetime.now().strftime("%d/%m/%Y")
		print("The Alarm Date is : ", present_date)
		print('The Alarm Time is : ', present_time)
		if present_time == set_timer:
			print("It's time to wake up!")
			winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
			break


def actual_time():
	set_timer = f"{set_hour.get()}:{set_min.get()}:{set_sec.get()}"
	alarm_clock(set_timer)


clock = Tk()

clock.title('Alarm Clock')
clock.geometry("400x200")
clock.configure(bg='azure2')
clock.resizable(0, 0)
Label(clock, text='Enter time in 24 hour format!', fg='steel blue', bg='thistle1', font='Arial').place(x=60, y=120)

Label(clock, text='Hour   Min   Sec', font=60).place(x=120, y=5)

Label(clock, text='When to wake you up: ', fg='blue', relief='solid', font=('Gungsuh', 7, 'bold')).place(x=0, y=29)

set_hour = StringVar()
set_min = StringVar()
set_sec = StringVar()

# Time to set the alarm clock
Entry(clock, textvariable=set_hour, bg='pink', width=15).place(x=120,y=30)
Entry(clock, textvariable=set_min, bg='pink', width=15).place(x=170,y=30)
Entry(clock, textvariable=set_sec, bg='pink', width=8).place(x=220,y=30)

Button(clock, text='Set Alarm', fg='blue', width=10, command=actual_time, bg='thistle1').place(x=130, y=70)



clock.mainloop()