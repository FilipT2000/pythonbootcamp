
i=0 #podzielne przez 3
n=0 #podizlene przez 5
for x in range(101):
    if x%3 == 0 or x%5 == 0:
        print(x, end=", ")
        i += 1

print(f"W przedziale jest {i} liczb podzielnych przez 3 lub 5")