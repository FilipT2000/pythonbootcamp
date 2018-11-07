
# funkcje jako argumenty moga przyjmowac tez inne funkcje ! :)

lista = [1,2,3,4,5,6,7]
#
# def przytnij(lista):
#     out = []
#     for x in lista:
#         start = lambda x: x > 3
#         stop = lambda x: x == 6
#         print(start)
#         if start == True:
#             out.append(x)
#         if stop == True:
#             return out
#
#
# print(lista)
# print(przytnij(lista))
# # print(out)
#


# przytnij(
#     data=[1,2,3,4,5,6,7]
#     start=lambda x: x > 3,
#     stop=lambda x: x ==6,
# )
# [4,5,6]


# ROZWIAZANIE


def przytnij(data, start, stop):
    result = []
    dodawac_do_listy = False

    for element in data:
        if start(element):
            dodawac_do_listy = True
        if dodawac_do_listy:
            result.append(element)
            if stop(element):
                break
    return result

# przytnij(lista, start, stop)
# print(result)

#warunke taki, ze wieksze niz 3

# out [False, False, False, True, True, True, True]
#
# def bigger_than_3(liczba):
#     if liczba > 3:
#         return True
#     return False
#
#
# def sprawdzam_czy_wieksze_niz_3(lista):
#     out = []
#     for element in lista
#         out.append(bigger_than_3(element))
#     return out
#
#
# def sprawdzam_czy_wieksze_niz_3(lista):
#     out = []
#     for element > 3:
#         if element > 3:
#             out.append(True)
#         else:
#             out.append(False)
#     return(out)
