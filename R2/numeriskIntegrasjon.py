#2b numerisk integrasjon

a = 1
b = 5
n = 100

def f(x):
    return x**2

vSum = 0
hSum = 0

#venstretilnærming
sum = 0
mSum = 0
delta_x = (b-a)/n

for i in range(1, n+1):
    x = a + (i-1)*delta_x
    areal = f(x)*delta_x
    sum += areal
    
    m = a + (i - 0.5) * delta_x  # midtpunkt
    mAreal = f(m)*delta_x
    mSum += mAreal
    
print(f"\nsum: {sum:.3f}, Midt: {mSum:.3f}")
vSum = sum


#høyretilnærming
sum = 0
mSum = 0

for i in range(n):
    x = a + (i+1)*delta_x
    areal = f(x)*delta_x
    sum += areal
    
    m = a + (i + 0.5) * delta_x  # midtpunkt
    mAreal = f(m)*delta_x
    mSum += mAreal
    
print(f"sum: {sum:.3f}, Midt: {mSum:.3f}")
hSum = sum

print(f"venstre/høyre snitt: {(vSum+hSum)/2:.3f}")



#trapesmetoden
sum = 0

for i in range(1, n+1):
    sum += ((f(a + (i-1)*delta_x)+f(a + (i)*delta_x))*delta_x)/2
    
print(f"Trapes: {sum:.3f}\n")
    
