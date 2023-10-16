from rich.traceback import install
install()


class Däggdjur():
    def __init__(self, termoregeleringstemperatur):
        self.termoregeleringstemperatur = termoregeleringstemperatur

    def amma(self):
        print("Ammar...")

class Landdjur():
    def __init__(self, ben):
        self.ben = ben

    def gå(self):
        print("Går...")

class Havsdjur():
    def __init__(self, maxdjup):
        self.maxdjup = maxdjup
    
    def simma(self):
        print("Simmar...")
    
class Ödla(Landdjur):
    def __init__(self, termoregeleringstemperatur, vikt):
        super().__init__(termoregeleringstemperatur)
        self.vikt = vikt
    
    def släppSvans(self):
        print("Du tappade svansen...")

class Häst(Däggdjur, Landdjur):
    def __init__(self, termoregeleringstemperatur, ben, maxhastighet):
        Landdjur.__init__(self, ben)
        Däggdjur.__init__(self, termoregeleringstemperatur)
        self.maxhastighet = maxhastighet

    def spring(self):
        print("Du springer!")

class Val(Däggdjur, Havsdjur):
    def __init__(self, termoregeleringstemperatur, maxdjup, storlek):
        Däggdjur.__init__(self,termoregeleringstemperatur)
        Havsdjur.__init__(self, maxdjup)
        self.storlek = storlek
    
    def gåUpp(self):
        print("Du går upp till ytan...")

class Fisk(Havsdjur):
    def __init__(self, maxdjup, färg):
        super().__init__(maxdjup)
        self.färg = färg
    
    def blubba(self):
        print("Du blåser bubblor...")

fisk = Fisk("30m", "grön")
häst = Häst("44 grader celcius", 4, "70km/h")

fisk.blubba()
fisk.simma()

häst.gå()
häst.spring()
print(häst.maxhastighet)