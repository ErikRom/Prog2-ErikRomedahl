def Bijele(input):
    antal_kungar = 1 - input[0] 
    antal_damer = 1 - input[1]
    antal_torn = 2 - input[2]
    antal_löpare = 2 - input[3]
    antal_hästar = 2 - input[4]
    antal_bönder = 8 - input[5]

    print(f"{antal_kungar} {antal_damer} {antal_torn} {antal_löpare} {antal_hästar} {antal_bönder}")

n = input()
n = n.split(" ")
heltal = list(map(int, n))

Bijele(heltal)