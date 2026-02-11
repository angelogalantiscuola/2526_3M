# Esercizio 51: Serie di Fibonacci con ricorsione

## Obiettivo
Implementare una funzione ricorsiva che calcola l'n-esimo numero della serie di Fibonacci, dove F(0) = 0, F(1) = 1, e F(n) = F(n-1) + F(n-2) per n > 1.

## Istruzioni
1. Definire una funzione `fibonacci(n)` che accetta un intero n (n >= 0) e restituisce l'n-esimo numero di Fibonacci.
2. Gestire i casi base: se n == 0, restituisci 0; se n == 1, restituisci 1.
3. Per n > 1, chiama ricorsivamente la funzione per F(n-1) e F(n-2), e somma i risultati.
4. Nel programma principale, chiedi all'utente un numero n e stampa il risultato di fibonacci(n).
5. Gestisci input non validi (es. n negativo) stampando un messaggio di errore.

## Esempi
- fibonacci(0) = 0
- fibonacci(1) = 1
- fibonacci(2) = 1 (1 + 0)
- fibonacci(3) = 2 (1 + 1)
- fibonacci(4) = 3 (2 + 1)
- fibonacci(5) = 5 (3 + 2)
- fibonacci(6) = 8 (5 + 3)

## Suggerimenti
- La ricorsione è semplice ma inefficiente per n grandi (es. n > 30), ma per questo esercizio va bene.
- Testa con piccoli valori: fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(5) = 5, fibonacci(10) = 55.
- Usa `int(input(...))` per leggere n, e gestisci eccezioni con try-except se necessario.