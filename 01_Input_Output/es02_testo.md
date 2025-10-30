# Esercizio 02: Saluto Interattivo

## Obiettivo
Imparare a gestire l'input dell'utente utilizzando la funzione `input()` e a convertire i tipi di dato (casting) in Python.

## Istruzioni
1. Definisci una costante `ANNO_CORRENTE` e assegnale il valore dell'anno attuale (ad esempio, 2025).
2. Utilizza la funzione `input()` per chiedere all'utente il suo nome e salva il risultato in una variabile chiamata `nome_utente`.
3. Utilizza nuovamente `input()` per chiedere all'utente il suo anno di nascita e salva il risultato in una variabile (ad esempio, `anno_nascita`).
4. Poiché l'input è sempre una stringa, converti l'anno di nascita in un numero intero utilizzando la funzione `int()` e salvalo in una nuova variabile chiamata `anno_nascita_int`.
5. Calcola l'età approssimativa dell'utente sottraendo l'anno di nascita dall'`ANNO_CORRENTE`. Salva il risultato in una variabile chiamata `eta_utente`.
6. Stampa un saluto personalizzato che includa il nome e l'età dell'utente. L'output desiderato dovrebbe essere simile a:  
   "Ciao [Nome Utente]! Quest'anno compi circa [Età Utente] anni."