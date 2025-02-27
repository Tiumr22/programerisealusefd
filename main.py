# file = open("myFile.txt","w")
# file.write("MyText")
# file.close()

import bookcreator as bookcreator
import bookactivity as bookativity
import fileReader as reader
import calculator as calculator

def main():
    print("1 - külalisteraamatr")
    print("2 - tegevusraamat")
    print("3 - reader")
    print("4 - id")
    userInput = input("Sinu valik: ")
    if userInput == "1":
        bookcreator.guestBook()
    elif userInput == "2":
        bookativity.actions()
    elif userInput == "3":
        userFile = input("milline sa tahad lugeda? ")
        reader.readFile(userFile)
    elif userInput == "4":
        calculator.calculator()
    else:
        print("vale valik")
        
main()