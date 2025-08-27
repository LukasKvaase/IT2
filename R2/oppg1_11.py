n = 10

#a
print("\na)")
a = 1
for ai in range(1, n+1):
    print(ai, 1/2*(ai+1))

#b
print("\nb)")
b = 1
for bi in range(1, n+1):
    print(bi, 2*bi)
    
#c
print("\nc)")
c = 1
for ci in range(1, 101):
    print(ci, 2**(ci-1))
    
#d
print("\nd)")
d = 1
for di in range(1, n+1):
    print(di, 2**(di-1)-1)
    

for p in range (1, 101):
    print(p, round((1/3*p**3+1/2*p**2+1/6*p)))