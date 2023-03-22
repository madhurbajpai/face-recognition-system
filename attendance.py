from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os 
import csv
from tkinter import filedialog
import mysql.connector
import cv2

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x650+0+60")
        self.root.title("Attendance Manager")
        
        #################variables
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        img = Image.open(r"images\human1.jpg")
        img = img.resize((800,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=105)
        
        #second image banner
        img1 = Image.open(r"images\human1.jpg")
        img1= img1.resize((800,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=105)
        
        #bg image
        img3 = Image.open(r"images\bg.png")
        img3 = img3.resize((1350,650),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_lbl = Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=105,width=1350,height=545)
        
        title_lbl = Label(bg_lbl, text="Attendance Recorder", font=("Terminal",35,"bold"), bg="aliceblue", fg="salmon")
        title_lbl.place(x=0,y=0, width=1350,height=45)
        
        main_frame = Frame(bg_lbl, bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1350,height=500)
        
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("Times New Roman",12,"bold"))
        Left_frame.place(x=7,y=10,width=690,height=460)
        
        img_left = Image.open(r"images\human1.jpg")
        img_left = img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=1,y=0,width=716,height=50)
        
        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=60,width=680,height=370)
        
        
        
        ###############labelentry
        
        attendanceId_label=Label(left_inside_frame,text="Attendance Id:",font=("Times New Remon",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("Times New Roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        rollLabel_label=Label(left_inside_frame,text="Roll:",font=("Times New Remon",12,"bold"),bg="white")
        rollLabel_label.grid(row=0,column=2,padx=10,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("Times New Roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        nameLabel_label=Label(left_inside_frame,text="Name:",font=("Times New Remon",12,"bold"),bg="white")
        nameLabel_label.grid(row=1,column=0,padx=10,sticky=W)
        
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("Times New Roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        depLabel_label=Label(left_inside_frame,text="Department:",font=("Times New Remon",12,"bold"),bg="white")
        depLabel_label.grid(row=1,column=2,padx=10,sticky=W)
        
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("Times New Roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        timeLabel_label=Label(left_inside_frame,text="Time:",font=("Times New Remon",12,"bold"),bg="white")
        timeLabel_label.grid(row=2,column=0,padx=10,sticky=W)
        
        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("Times New Roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        dateLabel_label=Label(left_inside_frame,text="Date:",font=("Times New Remon",12,"bold"),bg="white")
        dateLabel_label.grid(row=2,column=2,padx=10,sticky=W)
        
        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("Times New Roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        attendance_label=Label(left_inside_frame,text="Attendance:",font=("Times New Remon",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=10,sticky=W)
        
        atten_status=ttk.Combobox(left_inside_frame,width=16,textvariable=self.var_atten_attendance,font=("Times New Roman",13),state="readonly")
        atten_status["values"]=("Status","Present","Absent")
        atten_status.grid(row=3,column=1,padx=10,pady=5)
        atten_status.current(0)

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=660,height=40)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("Times New Roman",12,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("Times New Roman",12,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("Times New Roman",12,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("Times New Roman",12,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("Times New Roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=460)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=640,height=370)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
###########################fetch

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    #########export
    
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No DATA found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your DATA esported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()