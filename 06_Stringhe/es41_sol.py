# Esercizio 41: Applicazione pratica - Analizzatore di testo con cicli e dizionari
# Leggi un testo dall'utente.
# Usa metodi per analizzare: conta caratteri, parole, frasi.
# Formatta output con escape e slicing per riassunto.

testo = input("Inserisci un testo: ").strip()
if not testo:
    print("Errore: testo vuoto.")
    exit()

# Metodi e analisi
num_caratteri = len(testo)
parole = testo.split()
num_parole = len(parole)
frasi = testo.split(".")
num_frasi = len(frasi)


# Output formattato
print(
    f"Analisi testo:\n\tCaratteri: {num_caratteri}\n\tParole: {num_parole}\n\tFrasi: {num_frasi}\n\t"
)
