from tkinter import*
from tkinter import messagebox

window = Tk()

def func1() :
    if chk.get() == 0 :
        messagebox.showinfo("","체크버튼이 꺼졌어요")
    else : 
        messagebox.showinfo("", "체크버튼이 켜졌어요")

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable=chk, command = func1)

cb1.pack()

window.mainloop()

    
