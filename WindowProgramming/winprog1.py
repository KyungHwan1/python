from tkinter import*

PNList = ["시골 똥강아지1.gif","시골 똥강아지2.gif","시골 똥강아지3.gif","시골 똥강아지4.gif","시골 똥강아지5.gif",
             "시골 똥강아지6.gif","시골 똥강아지7.gif","시골 똥강아지8.gif","시골 똥강아지9.gif"]

num = 0

def clickNext() :
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file="C:\\Users\\lkh02\\OneDrive\\바탕 화면\\PYTHON실습\\WindowProgramming\\"
                       + PNList[num])
    iLabel.configure(image = photo)
    iLabel.image = photo
    TLabel.configure(text = PNList[num])

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    photo = PhotoImage(file="C:\\Users\\lkh02\\OneDrive\\바탕 화면\\PYTHON실습\\WindowProgramming\\" 
                       + PNList[num])
    iLabel.configure(image = photo)
    iLabel.image = photo
    TLabel.configure(text = PNList[num])

window = Tk()
window.geometry("500x250")
window.title("시골 똥강아지 모음집")

btnNext = Button(window, text = "다음>>", command=clickNext)
btnPrev = Button(window, text = "<<이전", command=clickPrev)

photo = PhotoImage(file="C:\\Users\\lkh02\\OneDrive\\바탕 화면\\PYTHON실습\\WindowProgramming\\" + PNList[0])
iLabel = Label(window, image = photo)
TLabel = Label(window, text = PNList[0])

btnNext.place(x= 310, y= 20)
TLabel.place(x=200, y =23)
btnPrev.place(x=140, y =20)
iLabel.place(x=220, y=100)

window.mainloop()

