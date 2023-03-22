from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("500x450+200+100")
        self.root.title("Help")
        
        
        img = Image.open(r"images\help.jpg")
        img = img.resize((500,450),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_lbl = Label(self.root,image=self.photoimg)
        bg_lbl.place(x=0,y=45,width=500,height=405)
        
        title_lbl = Label(self.root, text="Help", font=("Terminal",35,"bold"), bg="aliceblue", fg="salmon")
        title_lbl.place(x=0,y=0, width=500,height=45)
        
        desc_lbl = Label(bg_lbl, text="Contact Us", font=("Terminal",35,"bold"), bg="aliceblue", fg="salmon")
        desc_lbl.place(x=0,y=200, width=500,height=100)
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()