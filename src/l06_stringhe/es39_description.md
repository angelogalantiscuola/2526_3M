# Esercizio 39: Manipolazione di stringhe con liste e cicli

Scrivi un programma che chieda all'utente di inserire più parole separate da spazi. Per ciascuna parola, applica le seguenti operazioni usando cicli:

- **Slicing**: Estrai i primi 3 caratteri e gli ultimi 3.
- **Modifica**: Converti la parola in maiuscolo e rimuovi eventuali spazi.
- **Concatenazione**: Unisci tutte le parole modificate in una singola frase.

Stampa i dettagli per ciascuna parola (primi 3, ultimi 3, modificata) e la frase finale. Gestisci errori per input vuoti o parole con meno di 3 caratteri (salta quelle parole).

**Esempio di input/output:**
- Input: "ciao hi mondo python"
- Output:
Parola 'hi' troppo corta per slicing.
Parola: ciao -> Primi 3: cia, Ultimi 3: iao, Modificata: CIAO
Parola: mondo -> Primi 3: mon, Ultimi 3: ndo, Modificata: MONDO
Parola: python -> Primi 3: pyt, Ultimi 3: hon, Modificata: PYTHON
Frase concatenata: CIAO MONDO PYTHON