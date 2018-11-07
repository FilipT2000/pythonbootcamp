

class Animal: #klasa
    krolestwo = "Fauna" #atrybut klasowy
    def __init__(self, nazwa):
        self.nazwa = nazwa
    pass



zyrafa = Animal()  #instancja (egzemplarz) klasy
mysz = Animal()

print(type(zyrafa))
print(zyrafa.krolestwo)