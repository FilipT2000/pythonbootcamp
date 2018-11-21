from random import randint
from przedmiot import Przedmiot

# randint (1, 10)

class Postac:

    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []

    @property
    def atak(self):
        wynik = self.moc_ataku()
        for i in self.ekwipunek:
            wynik += i.bonus_atk
        return wynik

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.")

    def __str__(self):
        if self.czy_zyje():
            napis = "Ewkipunek:\n"
            for x in self.ekwipunek:
                napis += str(x) + "\n"
            return f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.\n" + napis
        else:
            return f"jestem {self.imie}, mam{self.atak} ataku i nie zyje"


    def wylecz(self, ile):
        if self.zdrowie > 0:
            self.zdrowie = self.zdrowie + ile
            if self.zdrowie > self.max_zdrowie:
                self.zdrowie = self.max_zdrowie
            print(f"Wyleczyłem się o {ile}, mam teraz {self.zdrowie}")
        if self.zdrowie <= 0:
            print(f"Na leczenie juz za późno, sorry")


    def obrazenia(self, obrazenia):
        self.zdrowie = self.zdrowie - obrazenia
        print(f"Auu, Otrzymałem cios o sile {obrazenia}")
        if self.zdrowie <= 0:
            self.zdrowie = 0
            return print("Game over")
        print(f"Mam teraz {self.zdrowie} zdrowia")

    def czy_zyje(self):
        if self.zdrowie > 0: #mozna tez zapisac po prostu: return self.zdrowie > 0
            return True
        return False

    def moc_ataku(self):
        moc = randint(self._atak//2, self._atak)
        return moc

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def atak_plus(self):
            cios = self.atak
            for i in self.ekwipunek:
                cios += i.bonus_atk
            return cios

    @staticmethod
    def walka(atakujacy, broniacy):
        print(f"Walka: {atakujacy.imie} vs {broniacy.imie}")
        runda = 0
        while atakujacy.czy_zyje() and broniacy.czy_zyje():
            runda += 1
            print(atakujacy)
            print(broniacy)
            print(f"Runda {runda}")
            atak_atakujacego = atakujacy.moc_ataku()
            atak_broniacego = broniacy.moc_ataku()
            broniacy.obrazenia(atakujacy.atak)
            print(f"{atakujacy.imie} uderza {broniacy.imie} za {atak_atakujacego} obrażeń")
            atakujacy.obrazenia(broniacy.atak)
            print(f"{broniacy.imie} uderza {atakujacy.imie} za {atak_broniacego} obrażeń")
        print("Koniec walki")

rufus = Postac("Rufus", 3, 100)
janusz = Postac("janusz", 4, 80)
miotla = Przedmiot("Miotła", 5)


# Postac.walka(rufus, janusz)

rufus.daj_przedmiot(miotla)
rufus.przedstaw_sie()
print(rufus)
# rufus.obrazenia(20)
print(rufus.czy_zyje())
rufus.wylecz(70)


print(f"bonus atk: {rufus.atak_plus()}")

def test_nowa_postac():
    postac = Postac("Albert", 1, 20)
    assert postac.imie == "Albert" and postac.atak == 1 and postac.zdrowie == 20 and postac.max_zdrowie == 20

def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac