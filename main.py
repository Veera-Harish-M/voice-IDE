from tkinter import *
import os
import sys
import tkinter.filedialog as file
import os.path
from os import path
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import speech_recognition as sr
import pyttsx3

global file_name
file_name=""
global first_click
first_click=True
def main_win():
    
    def new_file(event=None):
        main_win()
        

    def openfile(event=None):
        if not text.compare("end-1c", "==", "1.0"):
            file_save()
        ftypes = [('Python files', '*.py'), ('All files', '*'),("Text Files","*.txt")]
        fn = file.askopenfilename(filetypes=ftypes, title="Open File")
        print(fn)
        file_name=str(fn)
        win.title("INVOCO :) Coding Made Simple-"+file_name)
        try:
            text.delete('1.0',END)
            f = open(fn, "r").read()
            text.insert(INSERT,str(f))
            f.close()
        except:
            return

    def file_saveas(event=None):
        ftypes = [('Python files', '*.py'), ('All files', '*'),("Text Files","*.txt")]
        f = file.asksaveasfile(filetypes=ftypes, mode='w', defaultextension=".txt")
        global file_name
        file_name=f.name
        win.title("INVOCO :) Coding Made Simple-"+file_name)
        if f is None: 
            return
        
        text2save = str(text.get(1.0, END)) 
        f.write(text2save)
        f.close()

    def file_save(event=None):
        try:
            global file_name
            if path.exists(file_name):
                open(file_name,"w").close()
                f=open(file_name,"r+")
                text2save = str(text.get(1.0, END))
                f.write(text2save)
                f.close()
            if not file_name:
                file_saveas()
        except:
            return

    def on_entry_click(event):
        global first_click
        if first_click:
            first_click=False
            ins_bot.delete(1.0,END)
            ins_bot.config(fg = 'black')

    def trainbot():
        """conv=open('training.txt','r').readlines()
        trainer = ListTrainer(chatbot)
        trainer.train(conv)
        
        conv=open('program.txt','r').readlines()
        trainer = ListTrainer(chatbot)
        trainer.train(conv)"""
        
    def speaking(text):
        engine=pyttsx3.init()
        voices=engine.getProperty("voices")
        engine.setProperty("voice",voices[1].id)
        engine.say(text)
        engine.runAndWait()    
        

        
    def keys_in():
        txt=str(ins_bot.get(1.0, END))
        t_bot.configure(state='normal')
        t_bot.insert(INSERT,str("\nYOU:"+txt))
        t_bot.configure(state='disabled')
        ins_bot.delete(1.0,END)
        if txt=="exit":
            speaking("Thanks for using Invoco")
            return
        if txt!= "I'm a learner Say Clearly":
            w=str(chatbot.get_response(txt))
            s=""
            for i in list(w):
                s=s+i
                if i==';' or i=='{' :
                    s=s+"\n"
            s="\n"+s
            text.insert(INSERT,str(s))    
    
    def voice_in():
        while True:
            t_bot.configure(state='normal')
            t_bot.insert(INSERT,str("\nFriedy:Command ME"))
            t_bot.configure(state='disabled')
            speaking("I'm listening")
            
            r=sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
            try:
                txt=r.recognize_google(audio)
            except:
                txt="I'm a learner Say Clearly"
            
            t_bot.configure(state='normal')    
            t_bot.insert(INSERT,str("\nYOU:"+txt))
            t_bot.configure(state='disabled')
            speaking(txt)

            if txt=="exit":
                speaking("Thanks for using Invoco")
                return
            if txt!= "I'm a learner Say Clearly":
                w=str(chatbot.get_response(txt))
                s=""
                for i in list(w):
                    s=s+i
                    if i==';' or i=='{' :
                        s=s+"\n"
            
            text.insert(INSERT,str(s))
            

        
    win=Tk()
    win.title("INVOCO :) Coding Made Simple")
    win.state('zoomed')

    frame = Frame(win,width=150,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1)
    frame.pack(side=LEFT,fill=Y)
    l_bot=Label(frame,text="FRIEDY :) Coding Assistant ").pack()
    
    t_bot=Text(frame,state='disabled',width=25)
    t_bot.pack(fill=Y,expand=1,after=l_bot)
    t_bot.configure(state='normal')
    t_bot.insert(INSERT,"Welcome to Invoco,\nI'm Friedy :)\nyour coding assistant....\nInstruct Me\n\n")
    t_bot.configure(state='disabled')
    
    ph1=PhotoImage(file="mic.png").subsample(5,5)
    ph2=PhotoImage(file="key.png").subsample(7,7)

    icon_new=PhotoImage(file="newfile.png").subsample(20,20)
    icon_open=PhotoImage(file="open.png").subsample(20,20)
    icon_save=PhotoImage(file="save.png").subsample(20,20)
    icon_saveas=PhotoImage(file="saveas.png").subsample(20,20)
    icon_close=PhotoImage(file="close.png").subsample(20,20)
    icon_exit=PhotoImage(file="exit.png").subsample(20,20)

    icon_undo=PhotoImage(file="undo.png").subsample(20,20)
    icon_redo=PhotoImage(file="redo.png").subsample(20,20)
    icon_copy=PhotoImage(file="copy.png").subsample(20,20)
    icon_cut=PhotoImage(file="cut.png").subsample(20,20)
    icon_paste=PhotoImage(file="paste.png").subsample(20,20)
    icon_delete=PhotoImage(file="delete.png").subsample(20,20)
    icon_find=PhotoImage(file="find.png").subsample(20,20)
    icon_replace=PhotoImage(file="replace.png").subsample(20,20)
    icon_selectall=PhotoImage(file="select.png").subsample(20,20)

    icon_font=PhotoImage(file="font.png").subsample(20,20)

    icon_zoomin=PhotoImage(file="zoomin.png").subsample(20,20)
    icon_zoomout=PhotoImage(file="zoomout.png").subsample(20,20)
    icon_maximize=PhotoImage(file="maximize.png").subsample(20,20)
    icon_minimize=PhotoImage(file="minimize.png").subsample(20,20)
    icon_normalview=PhotoImage(file="normalview.png").subsample(20,20)

    icon_help=PhotoImage(file="help.png").subsample(20,20)
    icon_feedback=PhotoImage(file="feedback.png").subsample(20,20)
    
    icon_invoco=PhotoImage(file="invoco.png").subsample(20,20)
    icon_developer=PhotoImage(file="developer.png").subsample(20,20)
    icon_friedy=PhotoImage(file="friedy.png").subsample(20,20)

    icon_speak=PhotoImage(file="speak.png").subsample(20,20)

    
    
    bot_txt=Label(frame,text="INSTRUCT:").pack(after=t_bot)

    ins_bot=Text(frame,width=25,height=3)
    ins_bot.pack(fill=X,after=bot_txt)
    
    ins_bot.insert(INSERT, "Enter your Instruction...")
    ins_bot.bind('<FocusIn>', on_entry_click)
    ins_bot.config(fg = 'grey')
    
    btn=Button(frame,text="command",image=ph2,compound="left", command=keys_in).pack(fill=X,after=ins_bot)
    b=Button(frame,text="Speak",image=ph1,compound="left", command=voice_in).pack(fill=X,after=btn)

    text=Text(win)
    text.pack(side=LEFT,after=frame,expand=1,fill=BOTH)
    text.configure(wrap='none')
    text.insert(INSERT,"//Here comes your code...You can manually edit it :)\n//Happy Coding....\n//Team INVOCO :) coding made simple\n\n\n")
       
    scroll = Scrollbar(win,orient=VERTICAL, command=text.yview)
    text.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT,fill=Y)


    scroll1 = Scrollbar(win, orient=HORIZONTAL,command=text.xview)
    text.configure(xscrollcommand=scroll1.set)
    scroll1.pack(side=BOTTOM,fill=X,before=text)

    chatbot = ChatBot('friedy')
    trainbot()



    
    def donothing(event=None):
        print('doing nothing')

        

    menubar = Menu(win)
    
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New" ,image=icon_new,compound="left",accelerator="Ctrl+N", command=new_file)
    filemenu.add_command(label="Open",image=icon_open,compound="left", accelerator="Ctrl+O",command=openfile)
    filemenu.add_command(label="Save",image=icon_save,compound="left",accelerator="Ctrl+S", command=file_save)
    filemenu.add_command(label="SaveAs",image=icon_saveas,compound="left",accelerator="Ctrl+Shift+S", command=file_saveas)
    filemenu.add_command(label="Close",image=icon_close,compound="left",accelerator="Alt+F4", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",image=icon_exit,compound="left", accelerator="Ctrl+Q",command=donothing)
    menubar.add_cascade(label="File", menu=filemenu)


    win.bind_all("<Control-q>",donothing)
    win.bind_all("<Control-o>",openfile)
    win.bind_all("<Control-s>",file_save)
    win.bind_all("<Control-Shift-s>",file_saveas)



    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo",image=icon_undo,compound="left",accelerator="Ctrl+Z", command=donothing)
    editmenu.add_command(label="Redo",image=icon_redo,compound="left",accelerator="Ctrl+Y", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Cut",image=icon_cut,compound="left",accelerator="Ctrl+X", command=donothing)
    editmenu.add_command(label="Copy",image=icon_copy,compound="left",accelerator="Ctrl+C", command=donothing)
    editmenu.add_command(label="Paste",image=icon_paste,compound="left",accelerator="Ctrl+V", command=donothing)
    editmenu.add_command(label="Delete",image=icon_delete,compound="left",accelerator="Del", command=donothing)    
    editmenu.add_separator()
    editmenu.add_command(label="Find",image=icon_find,compound="left",accelerator="Ctrl+F", command=donothing)
    editmenu.add_command(label="Replace",image=icon_replace,compound="left",accelerator="Ctrl+H", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Select All",image=icon_selectall,compound="left",accelerator="Ctrl+A", command=donothing)   
    menubar.add_cascade(label="Edit", menu=editmenu)
    

    formatmenu=Menu(menubar,tearoff=0)
    formatmenu.add_command(label="Font",image=icon_font,compound="left",accelerator="Ctrl+F", command=donothing)
    menubar.add_cascade(label="Format", menu=formatmenu)

    viewmenu=Menu(menubar,tearoff=0)
    viewmenu.add_command(label="ZoomIn",image=icon_zoomin,compound="left",accelerator="Ctrl++", command=donothing)
    viewmenu.add_command(label="ZoomOut",image=icon_zoomout,compound="left",accelerator="Ctrl+-", command=donothing)
    viewmenu.add_separator()
    viewmenu.add_command(label="NormalView",image=icon_normalview,compound="left",accelerator="Ctrl+N", command=donothing)
    viewmenu.add_separator()
    viewmenu.add_command(label="Maximize",image=icon_maximize,compound="left",accelerator="Ctrl+>", command=donothing)
    viewmenu.add_command(label="Minimize",image=icon_minimize,compound="left",accelerator="Ctrl+<", command=donothing)
    menubar.add_cascade(label="View", menu=viewmenu)
    

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index",image=icon_help,accelerator="Ctrl+H",compound="left" ,command=donothing)
    helpmenu.add_command(label="Send feedback",image=icon_feedback, accelerator="Alt+1",compound="left",command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    aboutmenu = Menu(menubar, tearoff=0)
    aboutmenu.add_command(label="About INVOCO",image=icon_invoco,accelerator="Alt+2",compound="left", command=donothing)
    aboutmenu.add_command(label="About FRIEDY",image=icon_friedy,accelerator="Alt+3",compound="left", command=donothing)
    aboutmenu.add_command(label="About Developers",image=icon_developer,accelerator="Alt+4",compound="left", command=donothing)
    menubar.add_cascade(label="About", menu=aboutmenu)

    speakmenu= Menu(menubar, tearoff=0)
    speakmenu.add_command(label="Speak",image=icon_speak,accelerator="Alt+S",compound="left", command=donothing)
    menubar.add_cascade(label="Speak To Friedy", menu=speakmenu)    


    win.config(menu=menubar)
    win.mainloop()

main_win()
