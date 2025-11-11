# Esercizio 18: Stringhe più lunghe di X

## Obiettivo
Scrivere un programma Python che chieda all'utente il numero N di stringhe da inserire e un valore X (lunghezza minima). Successivamente, legga N stringhe dall'utente, inserisca in una lista solo quelle con lunghezza maggiore di X, conti quante sono tali stringhe e calcoli la lunghezza media delle stringhe filtrate.

## Istruzioni
1. Richiedere all'utente di inserire N (numero intero positivo di stringhe) e X (numero intero positivo per la lunghezza minima).
2. Utilizzare un ciclo per leggere ciascuna delle N stringhe dall'utente.
3. Per ogni stringa, controllare se la sua lunghezza è maggiore di X; se sì, aggiungerla a una lista.
4. Dopo aver processato tutte le stringhe, contare il numero di elementi nella lista (stringhe più lunghe di X).
5. Se la lista non è vuota, calcolare la lunghezza media delle stringhe nella lista (somma delle lunghezze diviso il numero di stringhe).
6. Gestire il caso in cui N sia 0 o negativo, stampando un messaggio di errore.
7. Gestire il caso in cui nessuna stringa sia più lunga di X, stampando un messaggio appropriato.
8. Stampare il numero di stringhe filtrate e la lunghezza media (se applicabile).

## Esempio
Per N=3, X=3, stringhe: "a", "abcd", "efghi"  
Stringhe filtrate: "abcd" (lunghezza 4), "efghi" (lunghezza 5)  
Numero: 2  
Lunghezza media: (4 + 5) / 2 = 4.5