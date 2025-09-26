

def calcSum():
    a1 = float(input("a1: "))
    k = float(input("k: "))
    n = int(input("n: "))
    sum = 0
    for i in range(n):
        sum += a1
        a1 *= k
    print(sum)

calcSum()