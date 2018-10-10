i=1
y=0
while True:
    x = input("Podaj temperaturę lub wpisz k by zakończyć")
    if x=="k":
        break
    x = int(x)
    y = (y + x)
    srednia = y/i
    i = i + 1
print(srednia)
