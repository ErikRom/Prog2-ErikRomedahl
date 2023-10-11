class Fordon():
    def kör(self):
        print("Nu kör vi!")

class Bil(Fordon):
    def tuta(self):
        print("Tuuut!!")

class Cykel(Fordon):
    def plinga(self):
        print("Pling Pling!!")

class Sportbil(Bil):
    def kör(self):
        print("Nu kör vi!")

b = Bil()
b.kör()
b.tuta()

c = Cykel()
c.kör()
c.plinga()

s = Sportbil()
s.kör()
s.tuta()