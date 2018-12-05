# import sys

# try:
#     print(sys.argv[1])
# except IndexError:
#     print("Zapomniałeś podać nazwe pliku")

plik = input(print("Podaj nazwę pliku"))

# with open(sys.argv[1]) as f:
with open(plik) as f:
    # i=0
    # for linia in f:
    #     i += 1
    #     print(f"{i}  {linia}")

    for i, line in enumerate(f):
        print(i, line, end="")