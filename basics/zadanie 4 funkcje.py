def foo(pierwszy, *reszta ):
    # print("pierwszy: ", pierwszy)
    # print("reszta", reszta)
    if reszta:
        return pierwszy + 2*reszta[-1]
    return(pierwszy)

print(foo(1,2,5,16))

# reszta = [1, 2, 5, "coś tam jeszcze"]
# print(1,2,5, "coś tam jeszcze")
# print(reszta)
# print(*reszta) #dzieki * funkcja wypakowuje argument - nie ma znakow postojowych, itp)

def druga_funkcja(**slownik):
        if "d" in slownik:
            return slownik['a'] + slownik['d']
        if slownik:
            return slownik['a']
        return "Zaden warunk nie był spełniony"

print('a', druga_funkcja(a=2))
print('a i d', druga_funkcja(a=2, b=2, c=3, d=4))
print('a i d drugi raz', druga_funkcja(a=2, b=2, c=3, d=4, zosia=5, adas=15))
print('a drugi raz ale bez d', druga_funkcja(a=2, b=2, c=3, zosia=5, adas=15))


co_na_co = {
    "Ala": "Kot",
    "kota": "Alę"
}


def zamien(jakis_tekst, **co_na_co):
    for klucz in co_na_co:
        jakis_tekst = jakis_tekst.replace(klucz, co_na_co[klucz])

    return jakis_tekst

print(zamien("Ala ma kota", Ala="kot", kota="Alę"))

print(zamien("Ala ma kota", **co_na_co))

slownik = dict(a=1, b=2, ma ="bije")
print(slownik)



