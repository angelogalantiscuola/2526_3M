# Esercizio 43: Conversione da Binario a Decimale

# Leggi una stringa binaria dall'utente
binario = input("Inserisci una stringa binaria: ").strip()

# Inizializza il numero decimale
decimale = 0

# Usa un ciclo for per convertire
for bit in binario:
    decimale = decimale * 2 + int(bit)

# Stampa il numero decimale
print(f"Numero decimale: {decimale}")
