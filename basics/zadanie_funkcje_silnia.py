

x = int(input("Podaj liczbę: "))

# Dobrze działa, ale nie to rozwiązanie
# def silnia(x):
#     s = 1
#     for i in range(1,x+1):
#         s = s*i
#         x = s
#     return x
#
# print(silnia(x))


def silnia(liczba):
    if liczba == 0:
        return 1
    else:
        return liczba * silnia(liczba-1)


def test_silnia_dla_0():
    assert silnia(0) == 1


def test_silnia_dla_wieksze_od_0():
    assert silnia(2) == 2
    assert silnia()