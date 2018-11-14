class produkt():
    def __init__(self, nazwa, cena, id):
        self.nazwa = nazwa
        self.cena = cena
        self.id  = id

    def print_info(self):
        print(f"Produkt o id: {self.id}, nazwa: {self.nazwa}, cena: {self.cena}")

produkt1 = produkt("Cebula", 20, "i2")
produkt2 = produkt("Czosnek", 5, "i3")
produkt3 = produkt("Piwo", 2, "i4")

produkt1.print_info()
produkt2.print_info()
produkt3.print_info()


