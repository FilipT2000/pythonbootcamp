class Temperatura:

    def __init__(self, x):
        self.wartosc = x   # podloga sprawia, ze jest brane 20, a nie 300

    def __str__(self):
        return f"Temaperatura: {self._wartosc} stopni Celcjusza"

    @property
    def wartosc(self):
        print("getter")
        return self._wartosc

    @wartosc.setter
    def wartosc(self, x):
        print("setter")
        self._wartosc = x

x = Temperatura(20)
print(x)
x.wartosc = 300
print(x)
print(x.wartosc)

