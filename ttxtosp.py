
from tkinter import *
import PyPDF2
from tkinter import filedialog as fd


import  pyttsx3
#m=tkinter.Tk()
m=Tk()
m.iconbitmap(r'finallogo.ico')
ma=pyttsx3.init()#inslaction
ma.say("welcome to T T S")
ma.setProperty('rate', 160)
voices = ma.getProperty('voices')#getting the voice data
print(voices)
ma.setProperty('voice', voices[0].id)
ma.runAndWait()
#print("hello python")'''

def filesel():
    file=fd.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    fpr=Label(m,text=file)
    fpr.pack()
    if(file):
     file=open(file,'r')
     ff= file.read()
     print(ff)
     la=Label(m,text=ff)
     la.pack()



    ma=pyttsx3.init()#inslactio

    #page=file.extractText()
    ma.say(ff)
    ma.runAndWait()
#print("hello python")'''
m.title("T-T-S")
m.geometry('500x500')
Label(m,text="🅃🄴🅇🅃 🅃🄾 🅂🄿🄴🄴🄲🄷",font=1000).pack()

photo=PhotoImage(file='eua.png')
img=Label(image=photo)
img.pack()
Label(text="selcte ap df fle to read the data ",font=90).pack()

button1=Button(m,text="selec",font=60,fg="red" ,command=filesel).pack()



'''ma=pyttsx3.init()#inslaction
#ma.say("hello anil kumar sahoo")
ma.runAndWait()
#print("hello python")'''

m.mainloop()