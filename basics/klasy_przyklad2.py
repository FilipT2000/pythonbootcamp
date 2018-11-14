# Dziedizczenie !!!!


class Zwierz():
        def przedstaw_sie(self):
            print("nie wiem czym jestem")

class Pies(Zwierz):
    def przedstaw_sie(self):
        print("jestem psem")



z = Zwierz()
z.przedstaw_sie()
x = Pies()
x.przedstaw_sie()