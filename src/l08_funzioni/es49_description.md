# Esercizio 49: Gioco "Indovina il numero" con approccio top-down

## Obiettivo
Creare un gioco semplice dove l'utente deve indovinare un numero casuale generato dal computer, con feedback sui tentativi e contatore. Il programma deve essere risolto usando l'approccio top-down, decomponendo il problema principale in sottoproblemi più piccoli, ciascuno gestito da una funzione dedicata.

## Cos'è l'approccio top-down?
L'approccio top-down consiste nel dividere un problema complesso in sottoproblemi più semplici e indipendenti. Ogni sottoproblema viene risolto da una funzione separata, migliorando la leggibilità, la manutenibilità e il test del codice. In questo esercizio, il gioco è decomposto in funzioni per generazione, input, verifica, contatore e output.

## Istruzioni
1. Definire una funzione `genera_numero` che genera e restituisce un numero casuale tra 1 e 100.
2. Definire una funzione `chiedi_tentativo` che chiede all'utente di inserire un tentativo e lo restituisce come intero.
3. Definire una funzione `verifica_tentativo` che accetta il tentativo e il numero segreto, e restituisce una stringa: "corretto" se indovinato, "alto" se troppo alto, "basso" se troppo basso.
4. Definire una funzione `aggiorna_contatore` che incrementa e restituisce il numero di tentativi.
5. Definire una funzione `stampa_fine` che accetta i tentativi e il numero, e stampa un messaggio di vittoria.
6. Definire una funzione `main` che orchestra il gioco: genera il numero, gestisce il ciclo di tentativi, chiama le altre funzioni e termina quando indovinato.
7. Nel ciclo principale, usa un `while True` per continuare fino a indovinamento, chiamando le funzioni appropriate.

## Suggerimenti
- Usa il modulo `random` per generare il numero (importalo all'inizio).
- Gestisci input non validi (es. non numeri) nella funzione `chiedi_tentativo` con un try-except.
- Testa ogni funzione separatamente prima di integrarle.