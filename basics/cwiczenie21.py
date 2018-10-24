liczby = [5,2,1,4,3]



min_ = liczby[0]
max_ = liczby[0]

# for i in range (len(liczby)):

for i in liczby:
    if i < min_:
        min_ = i
    if i > max_:
        max_ = i

print("Wartości", min_, max_)
print("indexy, czyli pozycje", liczby.index(min_), liczby.index(max_))

liczby[liczby.index(min_)]=max_
liczby[liczby.index(max_)]=min_

print(liczby)

# for x in liczby:
#     print(x)

# assert liczby ==