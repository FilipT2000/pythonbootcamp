napis = "ten $produkt kosztuje $cena"
napis2 = "Zajęcia z $przedmiot zostały odwołane"

co_na_co = {
    "produkt": "Samochód",
    "cena": "200"
}

def formatuj(napis, **co_na_co):
    for i in co_na_co:
        napis = napis.replace("$"+i, co_na_co[i])

    return napis

print(napis)

print(formatuj(napis,produkt = "Aaaaaa",cena = "12345"))

#
# co_na_co = {
#     "Ala": "Kot",
#     "kota": "Alę"
# }


#
# def zamien(jakis_tekst, **co_na_co):
#     for klucz in co_na_co:
#         jakis_tekst = jakis_tekst.replace(klucz, co_na_co[klucz])
#
#     return jakis_tekst



assert formatuj(napis, produkt="Samochód", cena="200") == "ten Samochód kosztuje 200"
assert formatuj(napis2, przedmiot="Fizyki") == "Zajęcia z Fizyki zostały odwołane"