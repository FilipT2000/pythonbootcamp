
x_ma = None
x_mi = None
while True:
    x = input("Podaj liczbę lub wciśnij 'n' by zakończyć ")
    if x == "n":
        break
    x=int(x)
    if x_ma is None or x > x_ma:
        x_ma = x
    if x_mi is None or x < x_mi:
        x_mi = x

if x_ma is None and x_mi is None:
    print('Hello')
else:
    print (f"Maksimum to: {x_ma}")
    print (f"Minimum to: {x_mi}")
