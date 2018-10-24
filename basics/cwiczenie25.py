
napis = input("podaj Twój napis: ").lower()
licznik = 0
znak = {}

for i in napis:
    licznik += 1
    print(i)
    if i in znak:
       znak[i]= znak[i] + 1
    else:
        znak[i]=1

print (f"liczba znaków to: {licznik}, w tym:")
for i in znak:
    print(f" {i} - {znak[i]}")
print(znak)

# liczniki['a'] = liczniki.get('a', 0)