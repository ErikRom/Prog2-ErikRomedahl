def printing(input):
    dagar = input
    maskiner = 1
    counter = 0

    while maskiner < dagar:
        if dagar/maskiner < maskiner + dagar/2 * maskiner:
            maskiner += 1
            counter += 1
        else:
            maskiner += 1
            counter += 1
    
    print(counter)

printing(5)