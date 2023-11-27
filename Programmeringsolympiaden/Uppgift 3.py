bokstaver = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
list = []

def hemligt_ord(list):
    list1 = []
    ord = []


    list = "".join(list)
    for i in list:
        list1.append(i)


    for i in list1:
        if i in bokstaver:
            ord.append(i)

    ord = "".join(ord)
    print(f"Svar: {ord}")


n = int(input("n: "))
m = int(input("m: "))
for i in range(1, n+1):
    x = input(f"rad_{i}: ")
    list.append(x)


hemligt_ord(list)