from project_invoco_tk import main
import random
from tkinter import *
from tkinter.ttk import *


window=Tk()
i=int(0)
#To remove title bar
window.overrideredirect(1)

#to set screen center
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

x = (ws/2) - (853/2)    
y = (hs/2) - (480/2)
window.geometry('%dx%d+%d+%d' % (853, 480, x, y))

#To add image
photo1=PhotoImage(file="invoco.gif")
Label(window,image=photo1).grid(row=0,column=0,sticky=W)

progress = Progressbar(window, orient = HORIZONTAL, length = 815, mode = 'determinate') 

# Function responsible for the updation 
# of the progress bar value 
def bar(): 
	import time
	i=random.randint(1,20)
	progress['value'] = i
	var.set(str(i)+"%")
	window.update_idletasks() 
	time.sleep(1)

	i=random.randint(20,40)
	progress['value'] = i
	var.set(str(i)+"%")
	window.update_idletasks()
	time.sleep(1)

	i=random.randint(40,60)
	progress['value'] = i
	var.set(str(i)+"%")
	window.update_idletasks() 
	time.sleep(1)

	i=random.randint(60,80)
	progress['value'] = i
	var.set(str(i)+"%")
	window.update_idletasks() 
	time.sleep(1)

	i=random.randint(80,90)
	progress['value'] = i
	var.set(str(i)+"%")
	window.update_idletasks() 
	time.sleep(1)
	
	i=random.randint(93,99)
	progress['value'] = i
	var.set(str(i)+"%")
	window.update_idletasks() 
	time.sleep(1)

	i=random.randint(100,100)
	progress['value'] = i
	var.set(str(i)+"%")
	window.update_idletasks() 
	time.sleep(1)
	
	progress['value'] = 100
	var.set("100%")
	i=100
	time.sleep(0.3)

	import pyttsx3
	engine=pyttsx3.init()
	voices=engine.getProperty("voices")
	engine.setProperty("voice",voices[1].id)
	engine.say("Welcome to invoco")
	engine.say("coding made simple")
	engine.say("i'm friedy, your coding assistant")
	engine.runAndWait()
	window.withdraw()
	main.main_win()
            
progress.place(x=2,y=415)
var = StringVar()
Label(window,textvariable=var, font="none 12").place(x=815,y=415)
var.set("0%")


    
# This button will initialize 
# the progress bar 
Button(window, text = "Let's code", command = bar).place(x=400,y=445)

window.mainloop()
