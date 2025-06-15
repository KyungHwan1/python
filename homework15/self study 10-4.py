from tkinter import *
from tkinter import messagebox

# 키보드 눌렸을 때 실행될 함수
def keyEvent(event):
    # Shift + 방향키가 눌렸는지 확인
    if event.state & 0x0001:  # Shift 키가 눌렸는지 확인
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + " + event.keysym)
        else:
            messagebox.showinfo("키보드 이벤트", "Shift + " + event.keysym + " 키는 처리되지 않음")
    else:
        try:
            messagebox.showinfo("키보드 이벤트", "눌린 키 : " + chr(event.keycode))
        except:
            messagebox.showinfo("키보드 이벤트", "일반 키 아님 (KeySym: " + event.keysym + ")")

# 윈도우 생성
window = Tk()

# 모든 키 입력에 대해 이벤트 처리
window.bind("<Key>", keyEvent)

# 메인 루프 실행
window.mainloop()
