# Esercizio 19: Stringhe che contengono una lettera e sono più lunghe di X

## Obiettivo
Scrivere un programma Python che chieda all'utente il numero N di stringhe da inserire, una lettera C e un valore X (lunghezza minima). Successivamente, legga N stringhe dall'utente, inserisca in una lista solo quelle che contengono la lettera C e hanno lunghezza maggiore di X, conti quante sono tali stringhe e calcoli la lunghezza minima delle stringhe filtrate.

## Istruzioni
1. Richiedere all'utente di inserire N (numero intero positivo di stringhe), C (una singola lettera) e X (numero intero positivo per la lunghezza minima).
2. Utilizzare un ciclo per leggere ciascuna delle N stringhe dall'utente.
3. Per ogni stringa, controllare se contiene la lettera C (usando `C in stringa`) e se la sua lunghezza è maggiore di X; se entrambe le condizioni sono vere, aggiungerla a una lista.
4. Dopo aver processato tutte le stringhe, contare il numero di elementi nella lista.
5. Se la lista non è ancora vuota, calcolare la lunghezza minima delle stringhe nella lista.
6. Gestire i casi di errore per N, C e X (N e X devono essere positivi, C deve essere una lettera).
7. Stampare la lista filtrata, il numero di stringhe e la lunghezza minima (se applicabile).

## Nota sull'istruzione `C in stringa`
L'operatore `in` in Python verifica se un elemento (in questo caso, il carattere C) è presente in una sequenza (la stringa). Restituisce `True` se C appare almeno una volta nella stringa, altrimenti `False`. È case-sensitive, quindi 'a' != 'A'.

## Esempio
Per N=3, C='a', X=3, stringhe: "ciao", "test", "palla"  
Stringhe filtrate: "ciao" (contiene 'a', lunghezza 4 > 3), "palla" (contiene 'a', lunghezza 5 > 3)  
Numero: 2  
Lunghezza minima: 4