 # slownik = {}
 # slownik = dict()
 # slownik["klucz"] = "wartosc"
 # slownik ma klucze i korespondujace (przyporzadkowane im) wartosci
 # slownik {"a": 1. "b":2}
 # slownik.items
 # slownik.keys
 # slownik.values
 # slownik
 # "a" in slownik   #/True lub False/

 # slownik {"pomidory": 10, "ziemniaki": 20}


# slownik["pomidory"] = 10
# slownik["ziemniaki"] = 20
# slownik["cebula"] = 32

# slownik.get("woda", "brak produktu") - podaj wartosc dla klucza "woda", a jak nie ma takiego klucza to podaj "brak produktu"


cennik = {"pomidory": 10, "ziemniaki": 20, "cebula": 12}
magazyn = {"pomidory": 10, "ziemniaki": 10, "cebula": 10}
koszyk = dict()
wartosc = 0

print("Dziś w sprzedaży:")
print()
for k in cennik:
     print(k)

print()

while True:
     print("Czy chcesz kupować? Wciśnij n by wyjść ze sklepu")
     zakup = input("Napisz, co kupujesz: ")
     if zakup == "n":
          print("Do widzenia. Zapraszamy ponownie")
          print("Twój koszyk to:")
          for zakup in koszyk:
               cena = int(koszyk[zakup] * cennik[zakup])
               print(f" - {zakup}: {koszyk[zakup]} kg {cena} PLN")
          print(f"Należność:, {wartosc} ")
          break
     if zakup in cennik:
          kg = float(input("ile kg?: "))
          if kg <= int(magazyn[zakup]):
               koszyk[zakup]= kg   #tutaj jakos trzeba dodoawac kolejne kg do koszyka - gdy kupujemy dwa razy to samo
               wartosc = wartosc + (kg * cennik[zakup])
               print(wartosc)
               magazyn[zakup] = int(magazyn[zakup] - kg)
          else:
               print("Sorry, nie mamy tyle w magazynie!")
     else:
          print("Nie mamy takiego produkt")
          print("_"*50)


