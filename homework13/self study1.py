inFp = None              # 입력 파일
inStr = ""               
lineNum = 1              

inFp = open("C:/Temp/data1.txt", "r")  # 파일 열기

while True:
    inStr = inFp.readline()           
    if inStr == "":                   
        break
    print("%d: %s" % (lineNum, inStr), end="")  
    lineNum += 1                      

inFp.close()  # 파일 닫기
