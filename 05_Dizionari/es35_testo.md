# Esercizio 35: Conteggio di frequenze in una lista

## Obiettivo
Creare un dizionario per contare la frequenza di ogni elemento in una lista data.

## Istruzioni
1. Definisci una lista di parole (es. ["rosso", "blu", "rosso", "verde", "blu"]).
2. Inizializza un dizionario vuoto per le frequenze.
3. Usa un ciclo per scorrere la lista: per ogni parola, incrementa il conteggio nel dizionario (usa `get()` per gestire chiavi nuove).
4. Stampa le frequenze usando `.items()` in formato "Parola: Conteggio".

## Nota
Il metodo `get(chiave, default)` restituisce il valore se la chiave esiste, altrimenti il default (utile per inizializzare a 0).

## Esempio
Per la lista ["rosso", "blu", "rosso"], output:
rosso: 2
blu: 1