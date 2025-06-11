inFp, outFp = None, None     
inStr = ""                 

# 소스, 타깃 파일명을 사용자로부터 입력받기
inFileName = input("소스 파일명을 입력하세요: ")
outFileName = input("타깃 파일명을 입력하세요: ")


inFp = open(inFileName, "r")
outFp = open(outFileName, "w")


inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

# 파일 닫기
inFp.close()
outFp.close()


print("--- %s 파일이 %s 파일로 복사되었음 ---" % (inFileName, outFileName))
