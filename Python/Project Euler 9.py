import math

b = 500
a = 499
c = math.sqrt(a**2+b**2)

while b > 0:
    if (a+b+c) == 1000:
        print(a*b*c)
        break
    
    a -= 1
    c = math.sqrt(a**2+b**2)

    if a == 1:
        b -= 1
        a = b-1