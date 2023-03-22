from tkinter import*
from tkinter import ttk
import tkinter
from datetime import datetime
from time import strftime
from tkinter import messagebox
from PIL import Image,ImageTk
from face_recognition import Face_Recognition
from student import Student
from developer import Developer
from help import Help
import os
import datetime
from attendance import Attendance
from train import Train

class Face_Recognition_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x730+0+0")
        self.root.title("Face Recognition System")
        
        
        #image banner
        
        #first image banner
        img = Image.open(r"images\human1.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl1 = Label(self.root,image=self.photoimg)
        f_lbl1.place(x=0,y=0,width=500,height=105)
        
        #second image banner
        img1 = Image.open(r"images\human1.jpg")
        img1= img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=105)
        
        #third image
        img2 = Image.open(r"images\human1.jpg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=105)
        
        #bg image
        img3 = Image.open(r"images\bg.jpg")
        img3 = img3.resize((1350,630),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_lbl = Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=100,width=1350,height=630)
        
        title_lbl = Label(bg_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("Terminal",35,"bold"), bg="aliceblue", fg="salmon")
        title_lbl.place(x=0,y=0, width=1350,height=45)
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl=Label(f_lbl1,font=("Terminal",11,"bold"), bg="aliceblue", fg="salmon")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        #student button
        img4 = Image.open(r"images\stud.jpg")
        img4 = img4.resize((290,280),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_lbl, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=210)
        
        b1b = Button(bg_lbl, text="Student Details",command=self.student_details,cursor="hand2", bg="#118DFF",fg="white")
        b1b.place(x=100,y=300,width=220,height=40)
        
        img5 = Image.open(r"images\face.png")
        img5 = img5.resize((250,260),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b2 = Button(bg_lbl, image=self.photoimg5,command=self.face_data,cursor="hand2")
        b2.place(x=400,y=100,width=220,height=210)
        
        b2b = Button(bg_lbl, text="Face Detector",command=self.face_data,cursor="hand2")
        b2b.place(x=400,y=300,width=220,height=40)
        
        img6 = Image.open(r"images\atten.jpg")
        img6 = img6.resize((280,260),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b3 = Button(bg_lbl, image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=700,y=100,width=220,height=210)
        
        b3b = Button(bg_lbl, text="Attendance",cursor="hand2",command=self.attendance_data)
        b3b.place(x=700,y=300,width=220,height=40)
        
        img7 = Image.open(r"images\help.jpg")
        img7 = img7.resize((280,260),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b4 = Button(bg_lbl, image=self.photoimg7,command=self.help_data,cursor="hand2")
        b4.place(x=1000,y=100,width=220,height=210)
        
        b4b = Button(bg_lbl, text="Help Desk",command=self.help_data,cursor="hand2")
        b4b.place(x=1000,y=300,width=220,height=40)
        
        img8 = Image.open(r"images\train.jpg")
        img8 = img8.resize((240,230),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b5 = Button(bg_lbl, image=self.photoimg8,command=self.train_data,cursor="hand2")
        b5.place(x=100,y=380,width=220,height=210)
        
        b5b = Button(bg_lbl, text="Train Data",command=self.train_data,cursor="hand2")
        b5b.place(x=100,y=580,width=220,height=40)
        
        img9 = Image.open(r"images\photo.jpg")
        img9 = img9.resize((240,230),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b6 = Button(bg_lbl, image=self.photoimg9,command=self.open_img,cursor="hand2")
        b6.place(x=400,y=380,width=220,height=210)
        
        b6b = Button(bg_lbl, text="Photos",command=self.open_img,cursor="hand2")
        b6b.place(x=400,y=580,width=220,height=40)
        
        img10 = Image.open(r"images\developer.jpg")
        img10 = img10.resize((240,230),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b7 = Button(bg_lbl, image=self.photoimg10,command=self.developer_data,cursor="hand2")
        b7.place(x=700,y=380,width=220,height=210)
        
        b7b = Button(bg_lbl, text="Developer",command=self.developer_data,cursor="hand2")
        b7b.place(x=700,y=580,width=220,height=40)
        
        img11 = Image.open(r"images\exit.jpg")
        img11 = img11.resize((240,230),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b8 = Button(bg_lbl, image=self.photoimg11,command=self.iExit,cursor="hand2")
        b8.place(x=1000,y=380,width=220,height=210)
        
        b8b = Button(bg_lbl, text="Exit",command=self.iExit,cursor="hand2")
        b8b.place(x=1000,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Exit","Are you sure to exit",parent=self.root)
        if iExit>0:
            self.root.destroy()
        else:
            return
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()
