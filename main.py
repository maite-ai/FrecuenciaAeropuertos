import random

airports = ["MAD", "JFK", "ORY", "EZE", "AMS", "FRA"]
probability = [0.25, 0.22, 0.18, 0.14, 0.11, 0.10]
n_airports = 100

airports_generated = random.choices(airports, probability, k=n_airports)

frequencies = {}

for airport in airports_generated:
    if airport in frequencies:
        frequencies[airport] += 1
    else:
        frequencies[airport] = 1


print(" Aeropuerto \t Frecuencia")
for airport, frequency in frequencies.items():
    print(f"{airport}\t\t{frequency}")
