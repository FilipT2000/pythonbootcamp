class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Employee(Osoba):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko)
        self.stawka = 100
        self.godzin = 0.0

    def register_time(self, godzin):
        self.godzin += godzin
        if godzin > 8:
            self.godzin += godzin - 8

    def pay_salary(self):
        wyplata = self.stawka * self.godzin
        self.godzin = 0.0
        return wyplata


class PremiumEmployee(Employee):

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, kwota):
        self.bonus += kwota



emp1 = PremiumEmployee("Jan", "Nowak", 50)
emp1.register_time(5)
emp1.register_time(10)
emp1.give_bonus(1000)
print(emp1.pay_salary())
print(emp1.pay_salary())
