# Esercizio 43: Analisi di Testo con Stringhe e Liste

# Leggi il testo dall'utente
testo = input("Inserisci un testo: ")

# Dividi il testo in parole
parole = testo.split()

# Inizializza il dizionario per i conteggi delle vocali
conteggi = {}

# Vocali da contare
vocali = "aeiou"

# Per ciascuna parola, conta le vocali
for parola in parole:
    parola_lower = parola.lower()
    conteggio = 0
    for v in vocali:
        conteggio += parola_lower.count(v)
    conteggi[parola] = conteggio

# Trova il massimo numero di vocali
if conteggi:
    max_vocali = max(conteggi.values())
    # Trova le parole con il massimo numero di vocali
    parole_max = []
    for p, c in conteggi.items():
        if c == max_vocali:
            parole_max.append(p)
    # Scegli la prima
    parola_max = parole_max[0]

    # Stampa i risultati
    print(f"Conteggi vocali: {conteggi}")
    print(f"Parola con più vocali: {parola_max} ({max_vocali} vocali)")
else:
    print("Nessuna parola trovata.")
