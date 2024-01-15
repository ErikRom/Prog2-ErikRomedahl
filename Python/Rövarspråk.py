konsonanter = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

ord = input("Skriv ditt ord här: ")

def rovarspråk(ord):
    nytt_ord = ""

    for bokstav in ord:
        if bokstav in konsonanter:
            nytt_ord += bokstav + "o" + bokstav
        else:
            nytt_ord += bokstav
    
    print(nytt_ord)

rovarspråk(ord)