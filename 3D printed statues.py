import math

def printing(n):
    counter = n
    maskiner = 1
    dagar = 0
    statyer = 0

    while statyer < counter:
        if counter/maskiner > 3:
            maskiner = maskiner*2
            dagar += 1
        else:
            dagar += math.ceil(counter/maskiner)
            statyer += counter
    
    print(dagar)

n = int(input())
printing(n)