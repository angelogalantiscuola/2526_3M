# Esercizio 21: Gestione Studenti con Nomi e Voti

# Definire le liste parallele
nomi: list[str] = ["Alice", "Bob", "Charlie"]
voti: list[int] = [8, 7, 9]

# Verifica che le liste abbiano la stessa lunghezza (opzionale, ma buona pratica)
if len(nomi) != len(voti):
    print("Errore: Le liste nomi e voti devono avere la stessa lunghezza.")
    exit()

# Calcolare la media
somma_voti: int = 0
for v in voti:
    somma_voti += v
numero_studenti: int = len(voti)

media: float = 0.0
if numero_studenti > 0:
    media: float = somma_voti / numero_studenti

# Trovare massimo e minimo
massimo: int = 0
minimo: int = 10

for v in voti:
    if v > massimo:
        massimo = v
    if v < minimo:
        minimo = v

# Stampare i risultati
print("Studenti:")
for i in range(len(nomi)):
    print(f"{nomi[i]}: {voti[i]}")

print(f"Media: {media}")
print(f"Massimo: {massimo}")
print(f"Minimo: {minimo}")
