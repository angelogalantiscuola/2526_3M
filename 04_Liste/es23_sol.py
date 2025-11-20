# Esercizio 23: Città con Nomi, Popolazione e Area

# Definire le liste parallele
nomi: list[str] = ["Roma", "Milano", "Napoli"]
popolazione: list[int] = [2800000, 1400000, 1000000]
area: list[float] = [1285.0, 181.0, 117.0]

# Verifica che le liste abbiano la stessa lunghezza
if len(nomi) != len(popolazione) or len(nomi) != len(area):
    print("Errore: Le liste devono avere la stessa lunghezza.")
    exit()

# Calcolare la densità per ogni città
densita: list[float] = []
for i in range(len(nomi)):
    d: float = popolazione[i] / area[i]
    densita.append(d)

# Trovare la città con densità massima
max_densita: float = -float("inf")
indice_max: int = -1
for i in range(len(densita)):
    if densita[i] > max_densita:
        max_densita = densita[i]
        indice_max = i

# Contare quante città hanno densità >1000
conteggio: int = 0
for d in densita:
    if d > 1000:
        conteggio += 1

# Stampare i risultati
print("Città:")
for i in range(len(nomi)):
    print(f"{nomi[i]}: {densita[i]:.2f} abitanti/km²")

print(f"Città con densità massima: {nomi[indice_max]}")
print(f"Città con densità >1000: {conteggio}")
