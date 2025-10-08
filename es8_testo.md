# Esercizio 08: Verifica anno bisestile

## Obiettivo
Scrivere un programma Python che determini se un anno fornito dall'utente è bisestile o meno, secondo le regole del calendario gregoriano.

## Istruzioni
1. Richiedere all'utente di inserire un anno (numero intero positivo).
2. Utilizzare l'operatore modulo (%) per verificare la divisibilità:
   - L'operatore % restituisce il resto della divisione intera (ad esempio, 10 % 3 = 1, poiché 10 ÷ 3 = 3 con resto 1).
   - Un anno è bisestile se è divisibile per 4, ma non per 100 a meno che sia divisibile anche per 400.
3. Stampare un messaggio chiaro che indichi se l'anno è bisestile o meno, ad esempio:  
   "L'anno [anno] è bisestile." o "L'anno [anno] non è bisestile."