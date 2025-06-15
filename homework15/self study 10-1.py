from tkinter import*
window = Tk()
window.title("시골 똥강아지들 ^^")

photo1 = PhotoImage(file = "C:\\Users\\lkh02\\OneDrive\\바탕 화면\\PYTHON실습\\WindowProgramming\\시골 똥강아지들.gif")
photo2 = PhotoImage(file = "C:\\Users\\lkh02\\OneDrive\\바탕 화면\\PYTHON실습\\homework15\\시골 똥강아지2.gif")

label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT)
label2.pack(side=RIGHT)

window.mainloop()