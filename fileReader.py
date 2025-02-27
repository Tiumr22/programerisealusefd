def readFile(fileName):
    file = open(fileName, "r", encoding="utf-8")
    print(file.read())
    file.close()
    