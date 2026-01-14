# Esercizio 44: Input Valido

## Obiettivo
Scrivere un programma che chieda all'utente di inserire un numero positivo e intero, ripetendo la richiesta finché non viene fornito un input valido.

## Istruzioni
- Usa un ciclo while per continuare a chiedere finché l'input non è un numero intero positivo.
- Quando valido, stampa il numero e esci.

## Esempio
Input: -5 (errore), 10 (valido)  
Output: Numero valido: 10

### Esempio con while True
Di seguito un template minimale che mostra la struttura di un ciclo infinito usato per richiedere input valido (non è la soluzione completa e non usa un blocco try/except):

```python
# template: ripeti finché la condizione non è soddisfatta
while True:
    valore = input("Inserisci un valore: ")  # leggi input
    # controlla se l'input soddisfa la condizione desiderata
    if <condizione_di_validita>:
        # azione quando l'input è valido
        break
    # azione quando l'input non è valido (messaggio, nuovo tentativo, ...)
```