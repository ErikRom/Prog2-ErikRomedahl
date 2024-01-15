class Elev:
    def __init__(self, namn, ålder, godkänd):
        self.namn = namn
        self.ålder = ålder
        self.godkänd = godkänd
    def presentera():
        print(f"Hej! Jag heter {person1.namn}")

person1 = Elev("Erik", 18, True)

if person1.godkänd == True:
    person1.glad = True # type: ignore

Elev.presentera()

class Bil:
    antalbilar = 0
    __maxHastighet = 0
    def __init__(self, maxHastighet):
        antalbilar += 1
    
    def bil1(maxHastighet):
        return self.__maxHastighet()
    
    def getMaxHastighet(self):
        return self.__maxHastighet
    
    def setMaxhastighet(self, maxHastighet):
        if type(maxHastighet) == int and maxHastighet > 0:
            self.__maxHastighet = maxHastighet
        else: print("Du måste ange ett positivt tal")
    
    def milestokm(miles):
        return miles * 1.609344