def Bijele(*input):
    pieces = input
    antal_kungar = 1 - pieces[0] 
    antal_damer = 1 - pieces[1]
    antal_torn = 2 - pieces[2]
    antal_löpare = 2 - pieces[3]
    antal_hästar = 2 - pieces[4]
    antal_bönder = 8 - pieces[5]

    print([antal_kungar, antal_damer, antal_torn, antal_löpare, antal_hästar, antal_bönder])

Bijele(1,2,4,3,2,7)