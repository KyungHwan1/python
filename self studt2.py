inFp = None                            # 입력 파일
inList, inStr = [], ""               
lineNum = 1                          

inFp = open("C:/Temp/data1.txt", "r") # 텍스트 파일 열기
inList = inFp.readlines()             

for inStr in inList:                  
    print("%d: %s" % (lineNum, inStr), end="")  
    lineNum += 1                      

inFp.close()                          # 파일 닫기
