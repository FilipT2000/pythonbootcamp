# zbior_a = {1, 2, 3, 4, 5, 6} # elementy musza byc unialne (nie liczy powtorzen)
# zbior_a.add(7) # dodaje nowy element, ktorgo nie bylo w zbiorze
# set(lista) # mozemy rzutowac inne na zbiory - wredy redukuje powtarzajce sie element w jeden element
#
# suma - |
# różnica - -
# iloczyn - &
# różnica symetryczna - ^

#
# a = {2,3,4}
# b = {4,5,6}
#
# print("suma", a | b)
# print("róznica", a - b)
# print("iloczyn", a & b)
# print("róznica symetryczna", a ^ b)
#
# print(list(range(1,100,2)))
# print(set(range(1,100,2)))

zbior = set()

while True:
    liczba = input("Podaj liczbę lub naciśnij n by zakończyć: ")
    if liczba == "n":
        print("Dziekujemy")
        break
    else:
        zbior.add(liczba)
print(zbior)

# Napisz program, który posortuje liczby w tablicyprzy wykorzystaniu algorytmu "sorotowanie przez wybieranie"