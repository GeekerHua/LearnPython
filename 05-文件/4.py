oldFile = input("请输入需要备份的文件名:")

index = oldFile.rfind('.')
newFilePath = oldFile[:index] + '[复件]' + oldFile[index:]

oldF = open(oldFile)
content = oldF.read()

newF = open(newFilePath, "w")
newF.write(content)

oldF.close()
newF.close()
