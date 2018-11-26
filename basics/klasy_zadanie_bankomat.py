
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

            elif sum(kasa_do_wyplaty) + i<= kasa:
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
bankomat.put_money([50, 100, 100, 200, 20])
print(bankomat.banknoty)
bankomat.withdraw(150)
print(bankomat.banknoty)
bankomat.withdraw(150)
print(bankomat.banknoty)
usun_banknoty()




