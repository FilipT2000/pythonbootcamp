
n=0

print("    ", end="")
for i in range(10):
    print(f"{i:3}", end=" ")
print()
print("      _____________________________________")

while n<=9:
    print(n, end=".  ")
    for i in range(10):
        print(f"{i*n:3}", end=" ")
    print()
    n += 1
