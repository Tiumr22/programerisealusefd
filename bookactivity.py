import datetime

def actions():
    name = input("Sinu nimi: ")
    actions = input("Sinu tegevus: ")
    time = datetime.datetime.now()
    text = f"Nimi:  {name}, Tegevus: {actions}, {time}"
    file = open("actions.txt", "a",encoding="utf-8")
    file.write(text)
    file.close()
    print("Activity oli salvestatu edukalt")