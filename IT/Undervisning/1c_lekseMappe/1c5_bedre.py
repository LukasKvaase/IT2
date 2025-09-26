# 29 med norske bokstaver
alfabeth = "abcdefghijklmnopqrstuvwxyzæøå"
# 335 små bokstaver
longText = "Oppgave 5 Finn en litt lang norsk tekst, for eksempel fra Wikipedia eller en nettavis, og finn antall forekomster av bokstavene a, e og k. Er bokstavene like vanlige? Tilpass programmet slik at du kan sjekke antall forekomster av alle bokstaver i det norske alfabetet. (Hint: Lag en tekst med det norske alfabetet som du går gjennom med en løkke. Sjekk deretter teksten din mot hver av bokstavene.) Hvilke bokstaver er vanligst?"

resultList = []

for alfabethLetter in alfabeth:
    tempCount = 0
    for textLetter in longText:
        if textLetter == alfabethLetter:
            tempCount += 1
    resultList.append([alfabethLetter, tempCount])

# lag prosent
letterCountInList = 0
for count in resultList:
    letterCountInList += count[1]

# kan ikke bruke max på vanlig måte da dette er en flerdimensional liste
highestCount = float("-inf")
lowestCount = float("inf")

for i, list in enumerate(resultList):
    resultList[i].append(float(f"{list[1]/letterCountInList*100:.2f}"))
    if resultList[i][1] > highestCount:
        highestCount = resultList[i][1]
    if resultList[i][1] < lowestCount:
        lowestCount = resultList[i][1]
for i in range (len(resultList)):
    if (resultList[i][1]) == highestCount:
        print(f"\033[32m{resultList[i][0]}: {resultList[i][1]:0>2} ({resultList[i][2]:0<5} %)\033[0m")
    elif(resultList[i][1]) == lowestCount:
        print(f"\033[7m{resultList[i][0]}: {resultList[i][1]:0>2} ({resultList[i][2]:0<5} %)\033[0m")
    else:
        print(f"{resultList[i][0]}: {resultList[i][1]:0>2} ({resultList[i][2]:0<5} %)")
