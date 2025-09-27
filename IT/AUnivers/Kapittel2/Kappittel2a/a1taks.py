def printAlert(string):
    print(f"\033[41m{string}\033[0m\n")

#taks 1
def task1():
    class Polygon:
        polygonCount = 1
        def __init__(self, sideCount:int, sideLenghtList:list = []):
            """
            Initializer for Polygon class, takes attributes sideCount
            """
            self._sideCount = sideCount
            self._sideLengthList = sideLenghtList
            self._polyId = Polygon.polygonCount
            Polygon.polygonCount += 1
            
        def defineSideLengths(self, sideList = []):
            """
            Method for defining the sides of a polygon. takes attribute self.
            """
            if len(sideList) < 1:
                for i in range (self._sideCount):
                    userInput = int(input(f"Write length of side number {i+1}: "))
                    self._sideLengthList.append(userInput)
            else:
                self._sideLengthList = sideList
        
        def calculateCircumfrence(self):
            """
            Method for calculating circumfrence of polygon. takes attribute self.
            """
            if len(self._sideLengthList) == 0:
                printAlert("List sideLengthList empty!")
            else:
                sum = 0
                for i in range(len(self._sideLengthList)):
                    sum += self._sideLengthList[i]
                return sum
        
        def __str__(self):
            """
            Method for printing information about given polygon. takes arttribute self.
            """
            if len(self._sideLengthList) < 1:
                outputString = f"Polygon {self._polyId} has {self._sideCount} sides."
            else:
                prettyList = ", ".join(str(side) for side in self._sideLengthList)
                outputString = f"Polygon {self._polyId} has {self._sideCount} sides. Sides are {prettyList}. And the circumfrence is {self.calculateCircumfrence()}"
            return outputString
            

                        
    octagone = Polygon(8)
    octagone.defineSideLengths([2,2,2,2,2,2,2,2])
    print(octagone.calculateCircumfrence())
    print(octagone)
    
    polygonList = [Polygon(4), Polygon(7), Polygon(5), Polygon(5)]
    for polygon in polygonList:
        print(polygon)



while True:
    print("\n- Tasks -")
    print("1: Task 1")


    choise = input("Choose task: ")
    if choise == "1":
        task1()
    elif choise == "0":
        print("Quiting program...")
        break
    else:
        print("Invalid, try again.")