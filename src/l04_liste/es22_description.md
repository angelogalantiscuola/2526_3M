# Esercizio 22: Classifica Squadre con Nomi e Punteggi

## Obiettivo
Definire due liste parallele: una con i nomi delle squadre e l'altra con i punteggi corrispondenti. Trovare la squadra vincente (con il punteggio più alto), calcolare la differenza di punteggio tra la prima e la seconda classificata, e stampare la classifica completa.

## Istruzioni
1. Definire una lista `squadre` con alcuni nomi di squadre (es. ["Milan", "Juventus", "Inter"]).
2. Definire una lista `punteggi` con i punteggi corrispondenti (es. [75, 80, 70]), assicurandosi che abbiano la stessa lunghezza.
3. Trovare la squadra con il punteggio più alto (con ciclo manuale, inizializzando con `-float('inf')` e tenendo traccia dell'indice).
4. Trovare la seconda squadra con il punteggio più alto (con un altro ciclo, escludendo la vincente).
5. Calcolare la differenza tra il punteggio della vincente e della seconda.
6. Stampare la classifica (squadre con punteggi), la vincente e la differenza.

## Nota sulle liste parallele
Le liste sono "collegate" per posizione: il nome all'indice i corrisponde al punteggio all'indice i.

## Esempio
Squadre: ["Milan", "Juventus", "Inter"]  
Punteggi: [75, 80, 70]  
Output:  
Classifica:  
Milan: 75  
Juventus: 80  
Inter: 70  
Vincente: Juventus  
Differenza con seconda: 5