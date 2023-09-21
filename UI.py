# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:49:17 2023

@author: 84908
"""

#from Model.Student import Student
#from Controller.StudentController import StudentController
import tkinter as tk

def onClick():
    #TODO
    #name = txtA.get("1.0", "end")
    #age = txtB.get("1.0", "end")
    #aStudent = Student(name, age)
    #StudentController().insertStudent(aStudent)
    cam_bien1 = txtA.get("1.0", "end")
    cam_bien2 = txtB.get("1.0", "end")
    return cam_bien1, cam_bien2

window = tk.Tk()
window.title("Python App")
window.geometry("600x400")

labelA = tk.Label(text="Sensor 1: ")
labelA.place(x=5,y=5,width=80,height=30)

txtA = tk.Text()
txtA.place(x=85,y=5,width=100,height=30)

labelB = tk.Label(text="Sensor 2: ")
labelB.place(x=5,y=35,width=80,height=30)

txtB = tk.Text()
txtB.place(x=85,y=35,width=100,height=30)

button = tk.Button(text="Save",command=onClick)
button.place(x=5,y=125,width=100,height=50)

#window.mainloop()