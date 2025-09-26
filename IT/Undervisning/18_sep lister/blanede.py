from random import randint

def createList(length):
    numList = []
    for i in range(length):
        numList.append(int(randint(0,100)))
    return numList

# oppgave 2
def oppgave2():
    numList = []

    for i in range(50):
        numList.append(randint(0,100))
        
    numList.sort()
    print(*numList)

    evenList = []
    oddList = []

    for num in numList:
        if num % 2 == 0:
            evenList.append(num)
        else:
            oddList.append(num)
            
    print(f"\nEven list:{evenList}\n")
    print(f"\Odd list:{oddList}\n")


    evenIndexList=[]
    for i, num in enumerate(numList):
        if i % 2 == 0:
            evenIndexList.append(num)
        else:
            pass
        
    print(*evenIndexList)

    numList.reverse()
    print(*numList)



# oppgave 3
def oppgave3():
    userInputs = []
    while True:
        userInput = int(input("Write whole number: "))
        if not userInputs.__contains__(userInput):
            userInputs.append(userInput)
            if len(userInputs) >= 10:
                break
        else:
            print(f"{userInput} already in list")
            
    print(f"Result list: {userInputs}")
    



#oppgave 4
def oppgave4():
    numList = createList(10)
    numList.sort()
    if len(numList) % 2 == 0:
        median = (numList[int(len(numList)/2)] + numList[(int(len(numList)/2))+1])/2
    else:
        median = numList[int(len(numList)/2)]
    print(median)
oppgave4()