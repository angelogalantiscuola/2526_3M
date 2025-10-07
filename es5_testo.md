# Esercizio 05: Equazione di secondo grado ax² + bx + c = 0

## Obiettivo
Scrivere un programma Python che risolva un'equazione di secondo grado della forma ax² + bx + c = 0, utilizzando il modulo `math` per il calcolo delle radici quadrate.

## Istruzioni
1. Importare il modulo `math` all'inizio del programma per accedere alla funzione `sqrt`.
2. Richiedere all'utente i valori dei coefficienti `a`, `b` e `c`.
3. Calcolare il discriminante `d` utilizzando la formula d = b² - 4ac.
4. In base al valore del discriminante:
   - Se d > 0, ci sono due soluzioni reali distinte:  
     x1 = (-b + sqrt(d)) / (2a)  
     x2 = (-b - sqrt(d)) / (2a)
   - Se d = 0, c'è una soluzione reale doppia:  
     x = -b / (2a)
   - Se d < 0, non ci sono soluzioni reali (soluzioni complesse).
5. Stampare le soluzioni in modo chiaro.

## Esempio
Per a = 1, b = 0, c = -4:  
d = 0 - 4*1*(-4) = 16 > 0  
x1 = (0 + 4) / 2 = 2  
x2 = (0 - 4) / 2 = -2