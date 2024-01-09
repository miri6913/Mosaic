import sys
import os
from tkinter import *
from anyio import CapacityLimiter
import cv2

# 창을 생성하고 설정하는 함수
def create_window():
    window = Tk()  # Tk()의 새 인스턴스 생성
    window.title("모자이크")
    window.geometry('550x200')

    def run():
        os.system('live_mosaic.py')


    def run2():
        os.system('image_mosaic.py')

    # 창 내에 버튼 생성
    btn1 = Button(window, text="실시간 모자이크", bg="black", fg="white", command=run)
    btn1.place(relx=0.5, rely=0.4, anchor=CENTER)

    btn2 = Button(window, text="이미지 모자이크", bg="black", fg="white", command=run2)
    btn2.place(relx=0.5, rely=0.5, anchor=CENTER)

    window.mainloop()  # Tkinter 메인 루프 시작

# 초기 창을 생성하기 위해 함수 호출
create_window()

