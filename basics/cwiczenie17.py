
i=1
lista =[]
while i<=10:
    x = input(f"Podaj liczbę, {i} lub wciśnij n by zakończyć:> ")
    i = i+1
    if x =="n":
        break
    x = int(x)
    lista.append(x)
print(lista)
if len(lista)==0:
    print("Nie podano danych")
else:
    srednia = sum(lista) / len(lista)
    print(f"Średnia to: {srednia}")