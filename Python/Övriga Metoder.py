def addera(*args):
    lista = list(args)
    produkt = lista[0]
    lista.pop(0)

    for i in lista:
        produkt *= i
    print(produkt)

addera(2, 5, 3, 2)


def food(edible, vegan=False):
    if vegan == True:
        print(f"soja{edible}")
    else:
        print(edible)

food("burgare", True)
