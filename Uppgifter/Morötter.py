import math

def morötter(t, m):
    counter = 0
    rötter = 40
    mrötter = 0
    trötter = 0
    
    while rötter > 0:
        if counter % t == 0:
            trötter += 1
            rötter -= 1
        if counter % m == 0:
            mrötter += 1
            rötter -= 1
        counter += 1
        if rötter == 1 and counter % m == 0 and counter % t == 0:
            break

    print(f"Tors morötter: {trötter} \n Mors morötter: {mrötter}")

morötter(19,18)