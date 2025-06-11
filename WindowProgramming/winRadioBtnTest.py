from tkinter import*

window = Tk()
window.geometry("300x200")

def func1() :
    if rad.get() == 1 :
        label1.configure(text = "파이썬")
    elif rad.get() == 2 :
        label1.configure(text = "C++")
    else :
        label1.configure(text = "Java")

rad = IntVar()
rb1 = Radiobutton(window, text = "파이썬", variable = rad, value = 1, command = func1 )
rb2 = Radiobutton(window, text = "C++", variable = rad, value = 2, command = func1 )
rb3 = Radiobutton(window, text = "Java", variable = rad, value = 3, command = func1 )

label1 = Label(window, text = "선택한 프로그래밍 언어 :", fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()


