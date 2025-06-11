outFp = None                          
outStr = ""                           

# 사용자로부터 파일명 입력받기
outFileName = input("파일명을 입력하세요: ")


outFp = open(outFileName, "w")


while True:
    outStr = input("내용 입력: ")
    if outStr != "":                   
        outFp.writelines(outStr + "\n")
    else:
        break                          

outFp.close()                           # 파일 닫기
print("--- 정상적으로 파일에 씀 ---")  
