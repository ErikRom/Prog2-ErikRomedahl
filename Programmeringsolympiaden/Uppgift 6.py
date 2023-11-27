bokstaver = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]

class Points():
    def __init__(self, poang):
        self.poang = int(poang)

siffra = 1
for i in bokstaver:
    i = Points(siffra)
    siffra += 1

def piano(stycke):
    dupelist = []
    list = []
    for i in stycke:
        if i not in list:
            list.append(i)
        else:
            dupelist.append(i)
        if i in dupelist:
            dupelist.append(i)
            list.remove(i)

    dupelist = sorted(dupelist)
    for i in dupelist:
        if i.poang - 

stycke = input("Stycke: ")
piano(stycke)