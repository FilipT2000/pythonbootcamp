# string = str(input("Podaj napis: "))
# znak_start = str(input("Podaj znak start: "))
# znak_end = str(input("Podaj znak endu: "))
#
# licznik = 0
#
# print(string)

def policz_znaki(napis, start="<", end=">"):
    for i in napis:
        if i == start:
            poziom += 1
        elif i == end:
            poziom -= 1
        else:
            ile_znakow = poziom
    return ile_znakow



# def policz_znaki(napis, start="<", end=">"):
#     pass

def test_policz_znaki_bez_znacznikow():
    assert policz_znaki('ala ma kota a kot ma ale') == 0

def test_policz_znaki_jeden_poziom_zaglebienie_standardowe_znaczniki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4

def test_policz_znaki_wiele_poziomow_zaglebienie_niestandardowe_znaczniki():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('ala [kota [a kot]] ma [ale]', start='[', end=']') == 18

def test_policz_znaki_standardowe_znaczniki_wiele_poziomow():
    assert policz_znaki('a <a<a<a>>>') == 6