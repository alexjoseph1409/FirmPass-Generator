import tkinter as tk
from tkinter import*
from string import *
from random import *
import time

#Defining main function responsible to build the Password
def  passgen():

	password_len=16
	possible_characters ="1a2s3d4f5g6h7j8k9l0Z_X-C!V@B$Q%Y^M*U"
	random_character_list = [choice(possible_characters) for i in range(password_len)]
	random_password = "".join(random_character_list)
	storedPW.set(random_password) 

#Creating the GUI Window
window = tk.Tk()
window.title("FirmPass Generator V1.0")
width = 550
height = 350
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))

#Code to display Current Time on the window
time1=''
clock = Label(window, font=('times', 20, 'bold'), bg='green')
clock.place(x=0,y=313)
def ticktick(): #Function to create a Digital Clock
	global time1
	time2 =time.strftime('%H:%M:%S')
	if time2 != time1:
		time1 = time2
		clock.config(text=time2)
	clock.after(200,ticktick) #calls the function again every 200 milliseconds
ticktick()
#Time Displaying code ends here

#Defining Variable to store Password Generated 
storedPW = tk.StringVar()

#Defining the Frame
Top = Frame(window, width=width)
Top.pack(side=TOP)
Form = Frame(window, width=width)
Form.pack(side=TOP)
Bot = Frame(window, width=width)
Bot.pack(side=BOTTOM)

#Labels available on the window
title = Label(Top, width=width, font=('arial', 15, 'bold'), text="<--------------------FirmPass Generator V1.0-------------------->", bd=1, relief=SOLID)
title.pack(fill=X)
password_label = Label(Form, font=('arial', 18), text="Password Generated", bd=10)
password_label.grid(row=0, pady=10)
instruction_label = Label(window, font=('arial bold',10 ), text='Select the Password and use "CTRL+C" Key to Copy it into Clipboard', bd=10)
instruction_label.place(x=45,y=150)

#Input/Entry Control Available on the window
password = Entry(Form, font=(18),textvariable=storedPW,width=24)
password.grid(row=0, column=1, columnspan=2)

#Buttons Available on the window
generate_button = Button(Form, text="Generate Now", width=25, command = passgen)
generate_button.grid(row=1, column=1)

#Initiating the Window
window.mainloop()
