s = 1
n = 50

for i in range(1,(n+1)):
    print(s, i)
    s += (i+1)**3
    
print(s)
