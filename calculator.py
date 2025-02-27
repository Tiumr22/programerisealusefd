def calculator():
    id1 = 1 
    for i in range(10):
        file = open("calculator.txt", "a",encoding="utf-8")
        nimi = userInput = input("sisesta nimi: ")
        vana = userInput = input("sisesta vana: ")
        text = f"id = {id1} ,Nimi:  {nimi}, Vana: {vana}\n"
        print(text)
        file.write(text)
        id1 += 1
        file.close()
        
    
        