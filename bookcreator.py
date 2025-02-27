def guestBook():
    name = input("Sinu nimi: ")
    comment = input("Sinu sõnum: ")
    text = f"Nimi:  {name}, Sõnum: {comment}"
    file = open("guestBook.txt", "a",encoding="utf-8")
    file.write(text)
    file.close()
    print("Sõnum oli salvestatu edukalt")