import random
import time

print("Välkommen!")

def Guess():
    print("Datorn kommer nu välja en siffra mellan 1-100")
    print("Du ska gissa så säger datorn om det är högre eller lägre")
    countGuess = 0
    AiNumber = random.randint(1,100)
    while True:
        userGuess = input("Skriv en gissning: ")
        if int(userGuess) == AiNumber:
            countGuess += 1
            print("Du gissade rätt! Svaret var " + userGuess + ". Du gissade rätt på " + str(countGuess) + " försök!")
            print("____________________________________________________________________________________________________________")
            Start()
        elif int(userGuess) > 100:
            print("Felaktig Gissning!")
            print("__________________________________________________")
            Start()
        elif int(userGuess) > AiNumber:
            print("Lägre!")
            countGuess += 1
        elif int(userGuess) < AiNumber:
            print("Högre!")
            countGuess += 1
def Choose():
    aicount = 0
    print("Du ska nu välja en siffra mellan 1-100 Datorn kommer sedan gissa.")
    userChoise = input(": ")
    if int(userChoise) > 100:
            print("Felaktig input!")
            print("__________________________________________________________")
            Start()
    else:
        low = 1
        high = 100
        while True:
            AiGuess = random.randint(low,high)
            aicount += 1
            if AiGuess == int(userChoise):
                print(AiGuess)
                print("Datorn gissade rätt! på " + str(aicount) + " försök!")
                print("______________________________________________________")
                Start()
            elif AiGuess > int(userChoise):
                print(AiGuess)
                print("Lägre!")
                high = AiGuess - 1
                time.sleep(1)
            elif AiGuess < int(userChoise):
                print(AiGuess)
                print("Högre!")
                low = AiGuess + 1
                time.sleep(1)
def Start():
    #val för användaren vilket program som ska startas
    print("Välj program genom att skriva in en siffra!")
    print("1. Datorn väljer nummer")
    print("2. Du väljer nummer")
    StartValue = input(": ")
    if StartValue ==  "1":
        Guess()

    elif StartValue == "2":
        Choose()

    else:
        print("Fel input!")
        print("________________________________________________________")
        time.sleep(1)
        Start()

Start()