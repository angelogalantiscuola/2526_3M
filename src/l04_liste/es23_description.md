# Esercizio 23: Città con Nomi, Popolazione e Area

## Obiettivo
Definire tre liste parallele: nomi delle città (string), popolazione (int), area in km² (float). Calcolare la densità abitativa (popolazione / area) per ogni città, trovare la città con densità massima, e contare quante città hanno densità >1000 abitanti/km².

## Istruzioni
1. Definire una lista `nomi` con nomi di città (es. ["Roma", "Milano", "Napoli"]).
2. Definire una lista `popolazione` con i valori corrispondenti (es. [2800000, 1400000, 1000000]).
3. Definire una lista `area` con le aree corrispondenti in km² (es. [1285.0, 181.0, 117.0]), assicurandosi che abbiano la stessa lunghezza.
4. Verificare che le tre liste abbiano la stessa lunghezza (usando len() e confronto).
5. Calcolare la densità per ogni città (popolazione / area) e memorizzarla in una lista `densita`.
6. Trovare la città con densità massima (con ciclo manuale, inizializzando con `-float('inf')` e tenendo traccia dell'indice).
7. Contare quante città hanno densità >3000 (con ciclo manuale).
8. Stampare la lista delle città con densità, la città con densità massima e il conteggio.

## Nota sulle liste parallele
Le tre liste sono collegate per posizione: il nome all'indice i corrisponde alla popolazione e area all'indice i.

## Nota su float('inf')
`float('inf')` rappresenta l'infinito positivo in Python, utile per inizializzare valori massimi senza usare numeri arbitrari come 999999. Garantisce che qualsiasi valore finito sia minore, e funziona anche con numeri negativi. `-float('inf')` è l'infinito negativo, perfetto per trovare massimi.

## Esempio
Nomi: ["Roma", "Milano", "Napoli"]  
Popolazione: [2800000, 1400000, 1000000]  
Area: [1285.0, 181.0, 117.0]  
Output:  
Città:  
Roma: 2178.99 abitanti/km²  
Milano: 7734.81 abitanti/km²  
Napoli: 8547.01 abitanti/km²  
Città con densità massima: Napoli  
Città con densità >3000: 2