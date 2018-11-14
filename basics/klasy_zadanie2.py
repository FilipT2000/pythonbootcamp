class Employee():
    def __init__(self, imie, nawisko, stawka):
        self.imie = "Jan"
        self.nazwisko = "Nowak"
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



emp1 = Employee("Jan", "Nowak", 50)
emp1.register_time(5)
emp1.register_time(10)
print(emp1.pay_salary())
print(emp1.pay_salary())
