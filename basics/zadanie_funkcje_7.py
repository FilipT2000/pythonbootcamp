

lista = [1,2,3, [4,5, [6, 7]], 7]

def splaszcz(lista):
    out = [] #definijuemy, ze out to lista
    for element in lista:
        if isinstance(element, list):
            out.extend(splaszcz(element))
        else:
            out.append(element)
    return(out)


# assert isinstance(lista[0], list)
# assert isinstance(lista[3], list)

# def splaszcz(lista):
#     for i in lista:

print(splaszcz(lista))

def test():
    assert splaszcz(lista) == [1,2,3,4,5,6,7,7]