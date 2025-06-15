from tkinter import*
import random

photoList = [None]*9
btnList = [None]*9
photonameList = ["시골 똥강아지1.gif","시골 똥강아지2.gif","시골 똥강아지3.gif","시골 똥강아지4.gif","시골 똥강아지5.gif",
             "시골 똥강아지6.gif","시골 똥강아지7.gif","시골 똥강아지8.gif","시골 똥강아지9.gif"]

xpos, ypos, num = 0, 0, 0

window = Tk()
window.geometry("210x210")

for i in range(0,9) :
    photoList[i] = PhotoImage(file = "C:\\Users\\lkh02\\OneDrive\\바탕 화면\\PYTHON실습\\WindowProgramming\\" + photonameList[i] )
    btnList[i] = Button(window, image = photoList[i])

random.shuffle(btnList)

for i in range(0,3) :
    for k in range(0,3) :
        btnList[num].place(x = xpos, y = ypos)
        num +=1
        xpos += 70
    xpos = 0
    ypos += 70

window.mainloop()