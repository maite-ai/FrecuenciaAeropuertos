import random

# Defino las listas de aeropuertos y de las probabilidades.
airports = ["MAD", "JFK", "ORY", "EZE", "AMS", "FRA"]
probability = [0.25, 0.22, 0.18, 0.14, 0.11, 0.10]
n_airports = 100

# Con la función «choices» del módulo «random», genero los 100 aeropuertos aleatorios. Como argumentos, le paso las listas de aeropuertos y de probabilidades, también el número de elementos con «k».
airports_generated = random.choices(airports, probability, k=n_airports)

# Creo un diccionario para almacenar los aeropuertos y agregar la frecuencia de repetición de cada uno.
frequencies = {}
for airport in airports_generated:
    frequencies[airport] = frequencies.get(airport, 0) + 1

# Imprimo los datos en formato tabla
print(" Aeropuerto \t Frecuencia")
for airport, frequency in frequencies.items():
    print(f"{airport}\t\t{frequency}")
