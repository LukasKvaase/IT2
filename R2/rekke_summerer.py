def calcSum(a1, n, d):
    sum = 0
    for i in range(n+1):
        sum += a1+(i-1)*d
        print(f"{i:<8}|{sum:8}|{a1+(i-1)*d:8}")
    return sum

def main():
    a1 = float(input("a1: "))
    n = int(input("n: "))
    d = float(input("d: "))
    print(f"{"n":<8}|{"sum":8}|{"an":8}\n--------|--------|--------")
    print(f"\nSummen er {calcSum(a1, n, d)}")
    
main()