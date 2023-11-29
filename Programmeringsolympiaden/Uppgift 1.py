def reduplikation(ord, upprepning):
    list = [ord]
    i = 0   
    while i < upprepning - 1:
        list.append(ord)
        i += 1
    list = "".join(list)
    print(f"Svar: {list}")

ord = input("Ord: ")
upprepning = int(input("Upprepning: "))

reduplikation(ord, upprepning)