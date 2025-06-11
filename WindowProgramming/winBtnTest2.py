from tkinter import*
from tkinter import messagebox

def sigoldogbutton() :
    messagebox.showinfo("시골똥강아지버튼","역시 강아지는 시골 똥강아지가 최고입니다.")

window = Tk()

Photo = PhotoImage(file = "C:\\Users\\lkh02\\OneDrive\\바탕 화면\\PYTHON실습\\WindowProgramming\\시골 똥강아지2.gif")
button1 = Button(window, image = Photo, command=sigoldogbutton)

button1.pack()

window.mainloop()