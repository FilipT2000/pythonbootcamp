# # for zmienna in x:
# #     print(zmienna)
#
# lista = [1,2,3]
# # for x in lista:
# #     print(x)
# #
# # for x in range(0, 10): #nawias otwarty z prawej strony, czyli 10 lelemntow od 0 - do 9)
# #     print(x)
#
# for x in enumerate(lista, 2):  #wymien elementy z listy numerujace je i zczynajac od numeru 2
#     print(x)
#
# (a,b) = (1,2) #przypisanie wartości do a i b - odpowiednio 1 i 2
# a,b = 1,2 # tez działa ;)))
#
# for idx, x in enumerate(lista, 2):
#     print(x)
#
# # Zadanie:
#
# lista=[1, -2, 4, -6, 8, 0, 15]
# i=0
# m=0
#
# for x in lista:
#     if x >0:
#         i=i+1
#     if x < 0:
#         m=m+1
# print(i)
# print(m)
#
# Koniec zadania
#
z = int(input("Podaj ile liczb"))
lista=[]
n=1
i=0
m=0
import random
while n<=z:
    r =random.randint(-100,100)
    lista.append(r)
    n=n+1
print(lista)

for x in lista:
    if x >0:
        i=i+1
    if x < 0:
        m=m+1
print(f"Liczb dodatnich: {i}")
print(f"Liczb ujemnych: {m}")