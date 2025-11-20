# Esercizio 22: Classifica Squadre con Nomi e Punteggi

# Definire le liste parallele
squadre: list[str] = ["Milan", "Juventus", "Inter"]
punteggi: list[int] = [75, 80, 70]

# Verifica che le liste abbiano la stessa lunghezza (opzionale, ma buona pratica)
if len(squadre) != len(punteggi):
    print("Errore: Le liste squadre e punteggi devono avere la stessa lunghezza.")
    exit()

# Trovare la squadra vincente
max_punteggio: float = -float("inf")
indice_vincente: int = -1
for i in range(len(punteggi)):
    if punteggi[i] > max_punteggio:
        max_punteggio = punteggi[i]
        indice_vincente = i

# Trovare la seconda classificata
secondo_max: float = -float("inf")
for i in range(len(punteggi)):
    if i != indice_vincente and punteggi[i] > secondo_max:
        secondo_max = punteggi[i]

# Calcolare la differenza
differenza: int = int(max_punteggio - secondo_max)

# Stampare i risultati
print("Classifica:")
for i in range(len(squadre)):
    print(f"{squadre[i]}: {punteggi[i]}")

print(f"Vincente: {squadre[indice_vincente]}")
print(f"Differenza con seconda: {differenza}")
