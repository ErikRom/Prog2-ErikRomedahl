class Djur():
    def __init__(self, namn):
        self.namn = namn
    
    def at(self):
        print(f"{self.namn} äter.")
    
    def sov(self):
        print(f"{self.namn} sover...")

class Fågel(Djur):
    def __init__(self, namn, vingspann):
        super().__init__(namn)
        self.vingspann = vingspann

class Fisk(Djur):
    def __init__(self, namn, maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup
    
    def simma(self):
        print(f"{self.namn} simmar!")


class Haj(Fisk):
    def __init__(self, namn, maxdjup, antalTänder):
        super().__init__(namn, maxdjup)
        self.antalTänder = antalTänder
    
    def at(self, djur):
        print(f"{self.namn} äter {djur.namn}.")


class Torsk(Fisk):
    def __init__(self, namn, maxdjup, hastighet):
        super().__init__(namn, maxdjup)
        self.hastighet = hastighet

def fånga(haj, torsk):
    if torsk.hastighet < 30 and haj.maxdjup >= torsk.maxdjup:
        return True
    else:
        return False

haj = Haj("Bertil", 100, 80)
torsk = Torsk("Nils", 90, 28)

print(fånga(haj, torsk))


haj.at(torsk)
haj.sov()
torsk.simma()
torsk.at()