from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+50")
        self.root.title("Train Data")
        
        
        title_lbl = Label(self.root, text="Train Data Set", font=("Terminal",35,"bold"), bg="aliceblue", fg="salmon")
        title_lbl.place(x=0,y=0, width=1200,height=45)
        
        img_top = Image.open(r"images\human1.jpg")
        img_top = img_top.resize((1200,130),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1200,height=300)
        
        b3b = Button(self.root, text="Train Data",command=self.train_classifier,cursor="hand2")
        b3b.place(x=0,y=340,width=1200,height=25)
        
        img_bottom = Image.open(r"images\human1.jpg")
        img_bottom = img_bottom.resize((1200,130),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=365,width=1200,height=325)
        
        
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image) .convert('L')#convert grayscale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        ############################train the
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Set Completed.")  
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()