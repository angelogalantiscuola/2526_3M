# Esercizio 26: Ordinamento manuale di una lista di numeri

## Obiettivo
Scrivere un programma Python che chieda all'utente quanti numeri inserire, li legga uno per uno, li memorizzi in una lista, e ordini la lista in ordine crescente utilizzando un algoritmo di ordinamento manuale (senza usare `sort()` o funzioni simili).

## Istruzioni
1. Richiedere all'utente di inserire il numero di valori da considerare (numero intero positivo).
2. Utilizzare un ciclo per leggere ciascun numero dall'utente e aggiungerlo a una lista vuota (inizializzata come `numeri = []`).
3. Implementare un ordinamento manuale usando cicli annidati.
4. Gestire il caso in cui la lista sia vuota (numero di valori = 0), stampando un messaggio di errore.
5. Stampare la lista originale e quella ordinata, ad esempio: "Lista originale: [numeri originali], Lista ordinata: [numeri ordinati]".

## Nota sull'algoritmo manuale
Esistono diversi modi per ordinare manualmente una lista. Il più semplice si chiama bubble sort, che confronta elementi adiacenti e li scambia se necessario.

## Esempio
Per 4 numeri: 3, 1, 4, 2  
Lista originale: [3, 1, 4, 2]  
Lista ordinata: [1, 2, 3, 4]