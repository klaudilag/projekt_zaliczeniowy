import random

#funkcja do zmiany kursu spółki
import sys


def randomStockChange():
    randomStockChange = random.randint(0,2)
    if(randomStockChange == 0):
        randomStockChange = random.uniform(-10,10)
    elif(randomStockChange == 1):
       randomStockChange = random.uniform(-30,-20)
    else:
        randomStockChange = random.uniform(20,30)
    return randomStockChange
isEnded = True
isRoundEnded = True
firstYear = 2000
buyingPrice = 100.0
sellingPrice = buyingPrice*0.98
stockHistory = [buyingPrice]
playerActions = []
print("Witaj na giełdzie!")
playerMoney = int(input("ile chcesz wpłacić?"))
while(isEnded):
    if(playerMoney<0):
        print("Masz za mało pieniędzy by wejść na giełdę!")
        isEnded = False
        isRoundEnded = False
    else:
        isRoundEnded = True
    while(isRoundEnded):
        playerActionsSum = 0.0
        for i in range(len(playerActions)):
            playerActionsSum += playerActions[i]
        playerBalance = 0.0
        for i in range(len(playerActions)):
            playerBalance += (playerActions[i] - sellingPrice) *-1
        print("wartosc konta:", playerMoney)
        print("wartość twoich akcji: ", playerActionsSum)
        print("Zarobek/Strata: ", playerBalance)
        print("wykres spolki")
        for i in range(len(stockHistory)):
            print(firstYear + i, ':', '#' * int(stockHistory[i] / 5), "Buy:",stockHistory[i],"Sell:" ,stockHistory[i]*0.98)
        choice = int(input("Czy chcesz kupić akcje tej spółki? 1 = Tak, 2 i więcej = nie"))
        while(choice==1):
            amountOfActions = int(input("Ile akcji chcesz zakupić?"))
            if(playerMoney >= buyingPrice*amountOfActions):
                for i in range(amountOfActions):
                    playerMoney -= buyingPrice
                    playerActions.append(buyingPrice)
                print("Zakupiłeś ", amountOfActions, " akcji za kwotę ", buyingPrice)
            else:
                print("nie stać cię na te akcje!")
            choice = int(input("Czy chcesz zakupić więcej akcji? 1 - tak, 2 - nie"))
        choice2 = int(input("Co chcesz teraz zrobić? 1-powtórzyć wybór, 2-przejść do kolejnego losowania, 3-wyświetlić zakupione akcje(Z możliwością ich sprzedaży)"))
        if (choice2 == 1):
            continue
        elif (choice2 == 2):
            choice = 2
        elif(choice2==3):
            if(len(playerActions) == 0):
                print("brak akcji do wyświetlenia!")
                choice2 = 1
            for i in range(len(playerActions)):
                print("Akcja numer", i + 1, "o wartości", "Buy:",playerActions[i], "Sell:", playerActions[i]*0.98)
        while(choice2==3):
            choice3 = int(input("Czy chcesz sprzedać jedną z posiadanych akcji? 1 - tak, 2 - nie"))
            if(choice3 == 1):
                quantityOfActionsToSell = int(input("ile akcji chcesz sprzedać?"))
                if(quantityOfActionsToSell > 0 and quantityOfActionsToSell <= len(playerActions)):
                    for i in range(quantityOfActionsToSell):
                        for i in range(len(playerActions)):
                            print("Akcja numer", i + 1, "o wartości", playerActions[i])
                        actionToSell = int(input("Podaj numer akcji do sprzedania: "))
                        if (actionToSell >= 1 and actionToSell <= len(playerActions) + 1):
                            print("pomyślnie sprzedano akcję numer", actionToSell, "o wartości", playerActions[actionToSell-1], "za kwotę" , sellingPrice, "!")
                            playerMoney += sellingPrice
                            playerActions.pop(actionToSell-1)
                        else:
                            print("błędny numer akcji!")
                else:
                    print("Brak takiej ilości akcji na koncie!")
            elif(choice3 == 2):
                choice2 = 2
                choice = 2
            else:
                print("błędny wybór! koniec programu.")
                sys.exit()


        isRoundEnded = False
        choiceToEndGame = int(input("Czy chcesz kontynuować grę? 1-Tak, 2-Zakończ"))
        if(choiceToEndGame == 2):
            isEnded = False
    if(buyingPrice < 0):
        print("firma upadła! koniec gry.")
        sys.exit()
    changeInPrice = randomStockChange()
    buyingPrice += changeInPrice
    sellingPrice = buyingPrice*0.98
    stockHistory.append(buyingPrice)
