# Esercizio 20: Conteggio Numeri Multipli di K tra A e B

## Obiettivo
Chiedere N (numero intero positivo), K (numero intero positivo), A e B (interi con A < B), leggere N numeri interi, inserire in una lista quelli multipli di K e compresi tra A e B (inclusi), contare quanti sono, calcolare la media se la lista non è vuota.

## Istruzioni
1. Richiedere all'utente di inserire N (numero intero positivo), K (numero intero positivo), A e B (interi con A < B).
2. Utilizzare un ciclo per leggere ciascuno dei N numeri interi dall'utente.
3. Per ogni numero, controllare se è multiplo di K (usando `numero % K == 0`) e se è compreso tra A e B (inclusi); se entrambe le condizioni sono vere, aggiungerlo a una lista.
4. Dopo aver processato tutti i numeri, contare il numero di elementi nella lista.
5. Se la lista non è vuota, calcolare la media dei numeri nella lista (somma / len).
6. Gestire i casi di errore per N, K, A e B (N e K devono essere positivi, A < B).
7. Stampare la lista filtrata, il numero di numeri e la media (se applicabile).

## Nota sull'istruzione `numero % K == 0`
L'operatore `%` in Python calcola il resto della divisione. Se il resto è 0, il numero è multiplo di K.

## Esempio
Per N=5, K=2, A=1, B=10, numeri: 2,4,6,8,12  
Numeri filtrati: 2 (2%2==0, 1<=2<=10), 4 (4%2==0, 1<=4<=10), 6 (6%2==0, 1<=6<=10), 8 (8%2==0, 1<=8<=10)  
Numero: 4  
Media: 5.0