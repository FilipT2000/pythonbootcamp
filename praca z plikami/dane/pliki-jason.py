import sys
import json


try:
    with open("pracownicy.json", "r") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []

op = input("Co chcesz zrobic? [d - dodaj, w - wypisz]: ")
# while True:
if op == "d":
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok_ur = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))
    pracownicy.append({"imię": imie, "nazwisko": nazwisko, "rok_urodzenia": rok_ur, "pensja": pensja})
    with open("pracownicy.json", "w") as plik:
        json.dump(pracownicy, plik)
    # with open(employees.py) as f:
    #     f.write

elif op == "w":
    for nr, p in enumerate(pracownicy, 1):
        print(f"-[{nr}] {p['imię']} {p['nazwisko']} - rok {p['rok_urodzenia']}, pensja {p['pensja']} PLN")





# obiekt = {"imie": "Jan", "wiek": 33}
#
# print(json.dumps(obiekt))
#
# napis = '{"imie": "Jan", "wiek": 33}'
#
# print(type(json.loads(napis)))