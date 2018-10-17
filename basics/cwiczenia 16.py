# krotka
# x = (1, "asdf", 7.5, (1,2))
# x[2] = "asdf"
# x[-1] - pytanie o ostatni element. W tym przypadku (1,2)
# x[-2] - 7.5
# x[1:3] - wez od pierwszego do drugiego (otwarty nawias z prawej , tzn. nie bierze trzeciego elelemntu)
#  x[:6:2] - wez od 6 elelemtu co drugigit push

x = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"Drugi element: {x[1]}")
print(f"Przedostatni element: {x[-2]}")
print(f"Od trzeciego do siódemgo: {x[2:7]}")
print(f"Co trzeci element: {x[::3]}")
print(f"Co drugi od końca: {x[::-2]}")

# git status
# git add (file)
# git commit -m "nazwa commita"
# git push origin devel
#