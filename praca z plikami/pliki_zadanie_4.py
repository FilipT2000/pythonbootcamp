import sys
import os

directory = sys.argv[1]

def tree(directory, wciecie=1):
    zawartosc = list(os.scandir(directory))
    for elem in os.scandir(directory):
        if elem == zawartosc[-1]:
            print(f"{wciecie * '|   ***'}{elem.name}")
        else:
            print(f"{wciecie * '|   -'}{elem.name}")
        if elem.is_dir():
            tree(elem, wciecie + 1)


tree(directory)

    # if elem.is_dir = True:
    #     print
