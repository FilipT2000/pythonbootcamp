from time import time

# x = time()
# print(time() - x)

# print(time()) #czas w sek. od 1 stycznia 1970 r.

def czas(func):
    def wrapper(*args, **kwargs):
        przed_wywolaniem = time()
        wynik = func(*args, **kwargs)
        po_wywolaniu = time()
        print(f"Czas wywolania funkcji: {po_wywolaniu - przed_wywolaniem} s.")
        return wynik
    return wrapper


def fib(x):
       if x <= 1:
           return x
       return fib(x-1) + (fib(x-2)


@czas
def funkcyja(x):
    return fib(x)

print(funkcyja(35))