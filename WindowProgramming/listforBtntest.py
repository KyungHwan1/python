from tkinter import*

window = Tk()

btnlist = [None]*3

for i in range(0,3) :
    btnlist[i] = Button(window, text = "버튼" + str(i+1))

for btn in btnlist :
    btn.pack(side=TOP, fill = X, padx = 30, pady = 30, ipadx = 70, ipady = 70)

window.mainloop()