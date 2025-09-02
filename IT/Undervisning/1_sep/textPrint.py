# påbegynt 1. september 2025

# imports
from time import sleep

# ansi farger
REDANSI = '\033[31m'
YELLOWANSI = '\033[33m'
GREENANSI = '\033[32m'

#linjer for å skrive ut
lines = [
    ["Never gonna give you up, never gonna let you down", 3],
    ["Never gonna run around and desert you", 1.5],
    ["Never gonna make you cry, never gonna say goodbye", 3],
    ["Never gonna tell a lie and hurt you", 1.5]
    ]

#progress bar funksjon. 3 farger
def progressBar(charsLength, time):
    print(REDANSI + "|", end="", flush=True)
    for i in range(charsLength):
        if i < charsLength/3:
            print(REDANSI + "#", end="", flush=True)
        elif i < charsLength/(3/2):
            print(YELLOWANSI + "#", end="", flush=True)
        else:
            print(GREENANSI + "#", end="", flush=True)
        sleep(time/charsLength)
    print(GREENANSI + "|", end="", flush=True)

#printer single line ut ifra line og time
def printLine(line, time):
    for i in range(0, len(line)):
        print(GREENANSI + line[i], end="", flush=True)
        if line[i] == " " or line[i] == ",":
            sleep((time*5)/len(line))
        else:
            sleep(time/((3/2)*len(line)))
    print("\n")
    sleep(1)
    
#bruker printLine() til å printe flere linjer
def printLines(lines):
    print("\n")
    for i in range(len(lines)):
        line = lines[i][0]
        time = float(lines[i][1])
        printLine(line, time)
        
#main
def main():
    progressBar(90, 2.0) # progress bar
    printLines(lines) # printer lines

main()