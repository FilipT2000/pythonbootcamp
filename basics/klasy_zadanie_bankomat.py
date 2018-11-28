class CashMachine:

    def __init__(self):
        self.banknoty = []

    def is_avaiable(self):
        if self.banknoty:
            return True
        return False

    def put_money(self, banknoty):
        self.banknoty.extend(banknoty)

    def withdraw(self, kasa):
        kasa_do_wyplaty = []
        # self.banknoty.sort()
        self.banknoty.sort(reverse=True)
        for i in self.banknoty:
            if i == kasa:
                self.banknoty.remove(i)
                return print(f"Wypłacono {kasa}")

            elif sum(kasa_do_wyplaty) + i <= kasa:
                kasa_do_wyplaty.append(i)
                if sum(kasa_do_wyplaty) == kasa:
                    return print(f"Wypłacono: {kasa_do_wyplaty}")

        return usun_banknoty(kasa_do_wyplaty)

    def usun_banknoty(self):
        self.banknoty.remove(kasa_do_wyplaty)

        # elif:
        #     for i in self.banknoty:

        pass

    def wallet(self):
        pass


bankomat = CashMachine()

operacja = input("Podaj typ operacji (W/ Y)")


if operacja == 'W':
    banknoty = input(print("Podaj jakie banknoty wpłacasz. Wpisz je rozdzielając spacja: "))
    banknoty = banknoty.split()
    print(banknoty)
    banknoty = [int(x) for x in banknoty]        #wyrażenie listowe [i**2 for i in range(10)]
    bankomat.put_money(banknoty)

# wypłata
if operacja == "Y":
    kwota_do_wyplaty = int(input("jaką kwotę chcesz wupłacic"))
    wyplacone = bankomat.withdraw(kwota_do_wyplaty)
    print(wyplacone)


#
# bankomat.put_money([50, 100, 100, 200, 20])
# print(bankomat.banknoty)
# bankomat.withdraw(150)
# print(bankomat.banknoty)
# bankomat.withdraw(150)
# print(bankomat.banknoty)
# usun_banknoty()
