# Esercizio 50: Gestore di lista della spesa con approccio top-down

## Obiettivo
Creare un programma per gestire una lista della spesa, permettendo di aggiungere elementi con prezzo, rimuoverli, visualizzarli e calcolare il totale. Il programma deve essere risolto usando l'approccio top-down, decomponendo il problema in sottoproblemi gestiti da funzioni separate.

## Istruzioni
1. Definire una funzione `aggiungi_elemento` che accetta una lista e aggiunge un nuovo elemento (nome e prezzo) dopo averli chiesti all'utente.
2. Definire una funzione `rimuovi_elemento` che accetta una lista e rimuove un elemento per nome, se presente.
3. Definire una funzione `visualizza_lista` che accetta una lista e stampa tutti gli elementi con i relativi prezzi.
4. Definire una funzione `calcola_totale` che accetta una lista e restituisce la somma dei prezzi.
5. Definire una funzione `main` che mostra un menu interattivo (aggiungi, rimuovi, visualizza, totale, esci) e chiama le altre funzioni in base alla scelta.
6. Usa una lista di dizionari per rappresentare gli elementi (es. [{"nome": "pane", "prezzo": 2.5}]).
7. Gestisci input non validi (es. prezzi non numerici) nelle funzioni appropriate.

## Suggerimenti
- Inizia con una lista vuota in `main`.
- Usa un ciclo `while` per il menu fino a scelta "esci".
- Ogni elemento è un dizionario con chiavi "nome" (str) e "prezzo" (float).