#opp

a = 1 # startverdi
n = 10 # ledd

#rekursivt
print(f"rekursivt\nLedd, Verdi")
for i in range(2, n+1):   #ledd 2 til n
    print(f"{i-1}, {a}")
    a = a + 2*i

#eskplisitt
print(f"eksplisitt\nLedd, Verdi")
for e in range(1, n+1):
    print(e, e**2 + e - 1)