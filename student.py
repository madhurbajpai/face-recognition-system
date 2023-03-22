from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x730+0+0")
        self.root.title("Face Recognition System")
        
        #==============================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        #first image banner
        img = Image.open(r"images\human1.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=105)
        
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
        
        title_lbl = Label(bg_lbl, text="Student Management System", font=("Terminal",35,"bold"), bg="aliceblue", fg="salmon")
        title_lbl.place(x=0,y=0, width=1350,height=45)
        
        main_frame = Frame(bg_lbl, bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1350,height=600)

        #left label frame

        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
        Left_frame.place(x=7,y=10,width=660,height=560)

        img_left = Image.open(r"images\human1.jpg")
        img_left = img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=1,y=0,width=716,height=50)
        #current course

        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("Times New Roman",12,"bold"))
        current_course_frame.place(x=2,y=60,width=650,height=120)

        dep_label=Label(current_course_frame,text="Department",font=("Times New Remon",12,"bold"),bg="white")

        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Times New Roman",12),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer Application","B.Tech. Cs","B.Tech. IT","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)


        course_label=Label(current_course_frame,text="Course",font=("Times New Remon",12,"bold"),bg="white")

        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Times New Roman",12),width=17,state="read only")
        course_combo["values"]=("Select Course","BCA","MCA","CSE","IT")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)


        year_label=Label(current_course_frame,text="Year",font=("Times New Remon",12,"bold"),bg="white")

        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Times New Roman",12),width=17,state="read only")
        year_combo["values"]=("Select year","2019-20","2020-21","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        sem_label=Label(current_course_frame,text="Semester",font=("Times New Remon",12,"bold"),bg="white")

        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Times New Roman",12),width=17,state="read only")
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        #class student
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Times New Roman",12,"bold"))
        class_student_frame.place(x=2,y=190,width=650,height=320)

        studentid_label=Label(class_student_frame,text="Student Id:",font=("Times New Remon",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("Times New Roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        studentname_label=Label(class_student_frame,text="Student Name:",font=("Times New Remon",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentn_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("Times New Roman",12,"bold"))
        studentn_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        class_div_label=Label(class_student_frame,text="Class Division:",font=("Times New Remon",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,sticky=W)

        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Times New Roman",12),width=18,state="read only")
        div_combo["values"]=("Select Division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        roll_no_label=Label(class_student_frame,text="Roll No:",font=("Times New Remon",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("Times New Roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        gender_label=Label(class_student_frame,text="Gender:",font=("Times New Remon",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Times New Roman",12),width=18,state="read only")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        dob_label=Label(class_student_frame,text="Date of Birth:",font=("Times New Remon",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("Times New Roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        email_label=Label(class_student_frame,text="Email:",font=("Times New Remon",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("Times New Roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        phone_label=Label(class_student_frame,text="Mob. No:",font=("Times New Remon",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("Times New Roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        address_label=Label(class_student_frame,text="Address:",font=("Times New Remon",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("Times New Roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        teacher_label=Label(class_student_frame,text="Teacher:",font=("Times New Remon",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("Times New Roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

       
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=640,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("Times New Roman",12,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("Times New Roman",12,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("Times New Roman",12,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("Times New Roman",12,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=250,width=640,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_data_set,width=34,font=("Times New Roman",12,"bold"),bg="green",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo",width=35,font=("Times New Roman",12,"bold"),bg="green",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        #right label frame

        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=560)
        
        img_right = Image.open(r"images\human1.jpg")
        img_right = img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        fr_lbl = Label(Right_frame,image=self.photoimg_right)
        fr_lbl.place(x=1,y=0,width=716,height=50)

        #======Search System===

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search")
        Search_frame.place(x=2,y=60,width=645,height=70)

        search_label=Label(Search_frame,text="Search By",bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,state="read only")
        search_combo["values"]=("Select","RollNo","PhoneNo")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=20)
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=10)
        search_btn.grid(row=0,column=3)

        showall_btn=Button(Search_frame,text="Show All",width=14)
        showall_btn.grid(row=0,column=4)

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=140,width=640,height=360)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","Id","Name","Div","RollNo","Gender","DateofBirth","Email","Mob","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Id",text="Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Div")
        self.student_table.heading("RollNo",text="RollNo")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DateofBirth",text="DateofBirth")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Mob",text="Mob")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"
        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("DateofBirth",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Mob",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",)
        self.student_table.column("Photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()                                            
                                                    
        
        #=====================================================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Messages are required.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="madhur123@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Students details had been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
    ###################fetch data######################
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="madhur123@",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    ########################get c
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    #######################update####################
    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Messages are required.",parent=self.root)
        
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="madhur123@",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student data updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
 #############################delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="madhur123@",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details delete successfully",parent=self.root)
            except  Exception as es:
                messagebox.showerror("Error",f"Due to{str(es)}",parent=self.root)                 
    ############reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")                

     #############################################generate  data set
    def generate_data_set(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Messages are required.",parent=self.root)
        
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="madhur123@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select *from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                 ##############################################Load face
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #MINIMUM NEIGHBOR=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(10)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows
                messagebox.showinfo("Result","generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
