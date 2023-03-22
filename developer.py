from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("900x450+200+100")
        self.root.title("Developer")
        
        
        img = Image.open(r"images\developer.jpg")
        img = img.resize((500,450),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_lbl = Label(self.root,image=self.photoimg)
        bg_lbl.place(x=0,y=45,width=500,height=405)
        
        title_lbl = Label(self.root, text="Developer", font=("Terminal",35,"bold"), bg="aliceblue", fg="salmon")
        title_lbl.place(x=0,y=0, width=900,height=45)
        
        main_frame = Frame(self.root,bd=2,bg="blue")
        main_frame.place(x=501,y=45,width=400,height=400)
        
        
        dev_label=Label(main_frame,text="About ")
        dev_label.place(x=0,y=5)
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()