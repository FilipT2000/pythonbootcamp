import json
from urllib.request import urlopen

lokacja = input(print("Podaj nazwe miejscowosci: "))
napis = 'https://www.metaweather.com/api/location/search/?query='
napis +=lokacja

print(napis)
with urlopen(napis) as file:
    miejscowosc = json.loads(file.read().decode("utf-8"))

print(miejscowosc[0]["title"])

id = miejscowosc[0]['woeid']
print(id)

print(f"Pogoda dla {lokacja}: ")

with urlopen(f"https://www.metaweather.com/api/location/{id}") as f:
    pogoda = json.loads(f.read().decode("utf-8"))

print(pogoda)
prognozy = pogoda["consolidated_weather"]
for prognoza in prognozy:
    print(f"Dzień: {prognoza['applicable_date']}")
    print(f"temp: {prognoza['the_temp']}")

