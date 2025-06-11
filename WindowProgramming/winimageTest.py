from tkinter import*
window = Tk()

photo = PhotoImage(file = "C:\\Users\\lkh02\\OneDrive\\바탕 화면\\PYTHON실습\\WindowProgramming\\시골 똥강아지들.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()