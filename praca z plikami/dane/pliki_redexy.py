 # REGULAR EXPRESSIONS - WYRAŻENIA REGULARNE
# regex101.com
# tekstasdfksn
# ..ks.

#  https://regex101.com/
#  !!!

import re
import sys

lista = str()
kody = []
maile = []
daty = []
try:
    with open("kodypocztowe.txt", "r") as plik:
        for linia in plik:
            lista += linia
            regex = re.compile("\d{2}-\d{3}")
            if regex.findall(linia):
                kody.append(regex.findall(linia))
            regex = re.compile(".+@.+")
            if regex.findall(linia):
                maile.append(regex.findall(linia))
            regex = re.compile("[0-3][0-9]{1,2} [A-Z][a-z]{2} 1\d{3}")
            if regex.findall(linia):
                daty.append(regex.findall(linia))


except FileNotFoundError:
    lista = []


# regex = re.compile("\d+")
# wynik = regex.findall("")

print(lista)
print(kody)
print(maile)
print(daty)