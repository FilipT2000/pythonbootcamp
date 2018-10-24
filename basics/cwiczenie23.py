napis = input("Podaj napis: ")
licznik = 0
czy_zliczac = False

for i in napis:
    if i == "<":
        czy_zliczac = True
    elif i == ">":
        czy_zliczac = False
    elif czy_zliczac:
        licznik +=1

print(licznik)
