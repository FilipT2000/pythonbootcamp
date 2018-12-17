import tkinter


# def jakas_funkcja():
#     wartosc = entry.get()
#     label.configure(text=wartosc)


def spalanie():
    cena = float(entry.get())
    spalanie = float(entry2.get())
    dystans = int(entry3.get())
    wynik = cena*dystans/100*spalanie
    print(wynik)
    label4.configure(text=wynik)


root = tkinter.Tk()
root.columnconfigure(1)

entry = tkinter.Entry(master=root)
entry.grid(row=0, column = 1, sticky=tkinter.EW)

entry2 = tkinter.Entry(master=root)
entry2.grid(row=1, column = 1)

entry3 = tkinter.Entry(master=root)
entry3.grid(row=2, column = 1)

label = tkinter.Label(master=root, text="Cena litra")
label.grid(row=0, column=0, sticky=tkinter.EW)

label2 = tkinter.Label(master=root, text="Spalanie na 100 km")
label2.grid(row=1, column=0)

label3 = tkinter.Label(master=root, text="Dystans")
label3.grid(row=2, column=0)

label4 = tkinter.Label(master=root, text="!")
label4.grid(row=3, column=1)

button = tkinter.Button(master=root, text="Policz", command=spalanie)
button.grid(row=3, column=0)




# button = tkinter.Button(master=root)
# button.grid(row=0, column=0)



root.mainloop()