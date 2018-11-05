# parametry = {"end": "Koniec", "sep": "_odstep_"}
#
# print("To jest pierwszy tekst", "To jest drugi tekst", **parametry)

def formatuj(*args, **kwargs):
    tekst = "\n".join(args)
    for k in kwargs:
        tekst = tekst.replace("$"+k, str(kwargs[k]))
    return tekst


def test_formatuj():
    assert formatuj(
        "koszt $cena PLN"
        "kwota $cena brutto",
        cena = 10,
    ) == "koszt 10 PLN\nkwota 10 brutto"
