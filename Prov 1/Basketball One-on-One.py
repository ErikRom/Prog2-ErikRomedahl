def winner(x):
    a = 0
    b = 0
    index = 0

    while a < 100:
        for i in x:

            if i == "A":
                if x[index+1] == "1":
                    a += 1
                else:
                    a += 2

            elif i == "B":
                if x[index+1] == "1":
                    b += 1
                else:
                    b += 2

            else:
                continue

            index += 1
        
        if a >= 11 and b + 1 < a:
            print("A")
            break

        elif b >= 11 and a + 1 < b:
            print("B")
            break

winner("A2B2A1B2A2B1A2B2A1B2A1A1B1A1A2")
