# Esercizio 36: Verifica e modifica con in

## Obiettivo
Verificare l'esistenza di una chiave in un dizionario e modificare o aggiungere valori di conseguenza.

## Istruzioni
1. Inizializza un dizionario di punteggi (es. {"Mario": 10, "Luca": 8}).
2. Chiedi all'utente di inserire un nome (stringa) e un nuovo punteggio (intero).
3. Usa `in` per verificare se il nome è già una chiave nel dizionario.
4. Se esiste, aggiorna il punteggio; altrimenti, aggiungilo come nuova coppia.
5. Stampa il dizionario aggiornato usando `.items()`.

## Nota
L'operatore `in` verifica la presenza di una chiave nel dizionario.

## Esempio
Se il dizionario iniziale è {"Mario": 10}, l'utente inserisce "Mario" e 15, diventa {"Mario": 15}. Se inserisce "Anna" e 12, diventa {"Mario": 10, "Anna": 12}.