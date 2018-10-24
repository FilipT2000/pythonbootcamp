# napis = "ala ma kota"
# print(napis[0])
# print("a" in napis)
# dir(napis) #sprawdza jakie można do danej zmiennej zastosowac metody. do uzycia w konsoli: napis = "Ala" dir(napis)

napis = input("podaj napis: ")
# samogloski = ["a","e","i","o","u","y","A","E","I","O","U","Y"] #mozna tez zrobic jako napis: samogloski ="aeiouyAEIOUY"

samogloski = "aeyuio"

x=0
for i in napis.lower():
    if i in samogloski:
        x+=1

    # if i == "a" or i == "e" or i == "i" or i=="o" or i=="u" or i=="y":
    #     x+=1
print(f"Jest dokładnie {x} samogłosek w podanym napisie")