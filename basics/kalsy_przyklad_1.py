class Osoba():
    imie = "Jan"
    nazwisko = "Kowalski"

    def __init__(self, imie, nazwisko):
        print("No siema")
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"nazwyam sie {self.imie} {self.nazwisko}")

    @staticmethod
    def metoda_statystyczna():
        print("metoda statystyczna")


obiekt = Osoba("Adam", "Małysz")
obiekt2 = Osoba("Adam", "mickiewicz")


obiekt2.imie = "karol"

print(obiekt.imie)
print(obiekt2.imie)

obiekt.przedstaw_sie()
obiekt2.przedstaw_sie()

Osoba.metoda_statystyczna()



print()