from random import randint

for i in range(5, 1, -1):
    print(i)
    
print()
    
for n in range(1, 10, randint(1,6)):
    print(n)

def inclusiveForLoop(startNum, endNum, change):
    print("\nfor loop\n")
    num = startNum
    if change > 0:
        while num <= endNum:
            print(num)
            num += change
    else:
        while num >= endNum:
            print(num)
            num += change
    
            
inclusiveForLoop(0, 10, 1)

print("\n\n")
for a in range(4, 10, 1):
    print(a)
    
print("\n\n")
for b in range(8, 1, -1):
    print(b)
    
print("\n\n")
for c in range(-23, 12, -2):
    print(c+1)
    
print("\n\n")
for d in range(1, 11, 1):
    d *= 3
    print(d)
    if(d%3 == 0):
        print()
    
