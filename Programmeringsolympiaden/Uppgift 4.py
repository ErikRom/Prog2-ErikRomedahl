import math

def klippningar(protein, k):
    bokstav  = []
    dupelist = []
    klippningar = 0
    for i in protein:
        if i not in bokstav:
            bokstav.append(i)
        else:
            dupelist.append(i)
    dubletter = set(dupelist)

    protein = protein.split()
    counter = 0
    i = 0
    for i in protein:
        while counter <= k:
            if i not in dubletter:
                protein.remove([i])
                counter += 1
            elif i in dubletter:
                klippningar += 1
                break
    print(protein)
        

    if len(dupelist) == 0:
        svar = math.ceil((len(protein)/k) - 1)
        if svar == 0:
            svar = 1
        print(f"Svar: {svar}")


protein = input("Protein: ")
k = int(input("k: "))

klippningar(protein, k)

# i == i + (i in range(1, (len(protein)) + 1))