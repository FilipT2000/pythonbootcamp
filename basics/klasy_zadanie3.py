class ElectricCar():
    def __init__(self, marka, max_zasieg):
        self.marka = "Tesla"
        self.zasieg = max_zasieg
        self.max_zasieg = max_zasieg

    def drive(self, dystans):
        wynik = self.zasieg - dystans
        if wynik < 0:
            wynik = self.zasieg
            self.zasieg = 0
            return wynik
        self.zasieg -= dystans
        return dystans

    def charge(self):
        self.zasieg = self.max_zasieg
        return self.zasieg


car = ElectricCar("Tesla", 100)
print(car.drive(300))
car.charge()



