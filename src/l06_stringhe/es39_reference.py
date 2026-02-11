# Esercizio 39: Manipolazione di stringhe con liste e cicli
# Chiedi all'utente di inserire più parole separate da spazi.
# Per ciascuna parola:
# - Applica slicing: primi 3 caratteri, ultimi 3.
# - Modifica: converti in maiuscolo e rimuovi spazi.
# - Concatena tutte le versioni modificate in una frase.
# Usa cicli per iterare sulla lista di parole.
# Gestisci errori per input vuoti o parole troppo corte.

parole_input = input("Inserisci più parole separate da spazi: ").strip()
if not parole_input:
    print("Errore: input vuoto.")
    exit()

parole = parole_input.split()
risultati = []

for parola in parole:
    if len(parola) < 3:
        print(f"Parola '{parola}' troppo corta per slicing.")
        continue
    primi = parola[:3]
    ultimi = parola[-3:]
    modificata = parola.upper().strip()
    risultati.append(modificata)
    print(
        f"Parola: {parola} -> Primi 3: {primi}, Ultimi 3: {ultimi}, Modificata: {modificata}"
    )

frase_concatenata = " ".join(risultati)
print(f"Frase concatenata: {frase_concatenata}")
