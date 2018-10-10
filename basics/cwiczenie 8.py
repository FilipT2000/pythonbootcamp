x = float(input("Wprowadź długość:"))
y = float(input("Wprowadź szerokość:"))
z = float(input("Wprowadź wysokość:"))

o = x*y*z
print(f"Objętość: {o} Większa od 1000 {o>1000}")

if o > 2000:
    print("Objętość większa niż 2 litry")
elif o > 1000:
    print("Objętość większa niż 1 litr")
else:
    print("Objętość mniejsza bądź równa litrowi")

#  0, "", {}. [], None sa traktowane w if jako False
#  1, "A", [1, ], (2, ), {1:'a'} jako True