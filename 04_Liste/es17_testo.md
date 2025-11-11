# Esercizio 17: Stringa più lunga

## Obiettivo
Scrivere un programma Python che chieda all'utente quante stringhe vuole inserire, legga le stringhe una per una e determini quale sia la più lunga.

## Istruzioni
1. Richiedere all'utente di inserire il numero di stringhe da considerare (intero non negativo).
2. Se l'input non è un intero valido o è negativo, stampare un messaggio di errore.
3. Utilizzare un ciclo per leggere ciascuna stringa e tenere traccia della stringa con lunghezza massima.
4. Al termine, stampare la stringa più lunga e la sua lunghezza.

## Esempio
Input: 3; inserisci: "ciao", "buongiorno", "ok"
Output: La stringa più lunga è: 'buongiorno' con 10 caratteri

# Esercizio 17: Numero più frequente (moda semplice)

## Obiettivo
Scrivere un programma Python che chieda all'utente quanti numeri inserire, li legga uno per uno, li memorizzi in una lista e trovi il numero che appare più volte (se ci sono più numeri con la stessa frequenza massima, scegliere il primo incontrato).

## Istruzioni
1. Richiedere all'utente di inserire il numero di valori da considerare (numero intero positivo).
2. Utilizzare un ciclo per leggere ciascun numero dall'utente e aggiungerlo a una lista vuota (inizializzata come `numeri = []`).
3. Dopo aver raccolto tutti i numeri, contare le frequenze usando un dizionario.
4. Trovare il numero con la frequenza massima.
5. Gestire il caso in cui la lista sia vuota, stampando un messaggio di errore.
6. Stampare il numero più frequente e quante volte appare, ad esempio: "Il numero più frequente è: [numero] (appare [frequenza] volte)".

### Nota: usare len() e confronti con cicli
Per esercizi che coinvolgono stringhe o liste può essere utile conoscere la funzione built-in `len()` che restituisce la lunghezza di una stringa (o il numero di elementi di una lista). Ad esempio, per trovare la stringa più lunga si può confrontare `len(s)` con la lunghezza corrente massima dentro un ciclo `for`.

Esempio di uso di `len()` su stringhe:

```python
s = "hello"
print(len(s))  # stampa 5
```

Questo permette di implementare l'algoritmo usando solo liste e cicli `for` senza funzioni avanzate.

## Esempio
Per 5 numeri: 1, 2, 2, 3, 2  
Il numero più frequente è: 2 (appare 3 volte).