# Esercizio 43: Conversione da Binario a Decimale

Scrivi un programma che converta una stringa binaria fornita dall'utente in un numero decimale.

- Leggi una stringa binaria dall'utente (composta solo da 0 e 1).
- Converti la stringa in numero decimale senza usare funzioni built-in come `int()` con base 2.
- Usa un ciclo `for` per iterare sui bit della stringa.
- Calcola il valore decimale sommando i contributi di ciascun bit (2^posizione).
- Gestisci il caso di stringa vuota o non valida.

Stampa il numero decimale corrispondente.

**Esempio di output:**
```
Inserisci una stringa binaria: 1010
Numero decimale: 10
```