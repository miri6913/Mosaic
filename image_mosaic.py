import cv2
import numpy as np
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import *
import io

root = Tk()
root.geometry('500x200')
global img

def open():
        global img
        root.filename =  filedialog.askopenfilename(initialdir = "window",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print (root.filename)
        img = cv2.imread(root.filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

        ratio = 0.04

        # 얼굴 객체 생성
        faces= face_cascade.detectMultiScale (gray, 1.05, 5)

        # 얼굴 주위에 직사각형 그림
        for x, y, w, h in faces:
                small = cv2.resize(img[y: y + h, x: x + w], dsize=(0, 0), fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
                img[y: y + h, x: x + w] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)

        cv2.imshow("smile", img)
        
def save():
        data = [('모든 파일', '*.*'),
                ('png 파일', '*.png')]
        file=root.filename = asksaveasfile(mode='w',initialdir = 'window', filetypes = data, defaultextension = data)
        a = file.name
        cv2.imwrite(a, img)
  
btn = Button(root, text="이미지 불러오기", bg="black", fg="white", command=open)

btn2 = Button(root, text="저장하기", bg="black", fg="white", command=save)

btn.pack()
btn2.pack()
root.mainloop()
        




    
