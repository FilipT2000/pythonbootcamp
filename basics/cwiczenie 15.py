# abs() - wartośc bezwzględna
# from <z jakiej biblioteki. import <co chcemy wyciagnac>
# from random import randint

from random import randint
graczX = randint(1, 10)

x_skarb = randint(1,10)
y_skarb = randint(1,10)
x_g = randint(1,10)
y_g = randint(1,10)
ox = abs(x_skarb - x_g)
oy = abs(y_skarb - y_g)
i = 0
kroki = 5

print("Znajdź skarb piratów!")
print(f"Jesteś tutaj: {x_g},{y_g}")
print(f"Skarb jest tutaj: {x_skarb},{y_skarb}")

while True:
    x = input("Wprowadź kierunek poszukiwań: w - góra, s - dół, a - lewo, d - prawo: ")
    i = i+1
    kroki = kroki - 1
    if x == "d":
        x_g = x_g + 1
    if x == "a":
        x_g = x_g - 1
    if x_g <1 or x_g > 10:
        print("Wyszedłeś poza planszę! Sorry!")
        break
    nox = abs(x_skarb - x_g)
    if nox < ox:
        print("Jesteś bliżej")
        ox = nox
    elif nox > ox:
        print("Jesteś dalej")
        ox = nox
    if x == "w":
        y_g = y_g + 1
    if x == "s":
        y_g = y_g - 1
    if y_g <1 or y_g > 10:
        print("Wyszedłeś poza planszę! Sorry!")
        break
    noy = abs(y_skarb - y_g)
    if noy < oy:
        print("Jesteś bliżej")
        oy = noy
    elif noy > oy:
        print("Jesteś dalej")
        oy = noy
    if noy == 0 and nox == 0:
        print(f"Znalazłeś skarb!! Znalazłeś go w {i} krokach!")
    elif kroki == 0:
        x_skarb = randint(1, 10)
        y_skarb = randint(1, 10)
        print(f"Czas uciekł. Masz {kroki} kroków. Piraci przenieśli skarb w inne miesjce")
        print(f"Teraz skarb jest tutaj: {x_skarb},{y_skarb}, a Ty tutaj: {x_g},{y_g}")

    # print (f"Jesteś tutaj {x_g}, {y_g}")
