# Esercizio 28: Dizionari con liste e calcolo medie

Scrivi un programma Python che:

1. Crea un dizionario dove le chiavi sono nomi di studenti (stringhe) e i valori sono liste di voti (numeri interi).
2. Crea il dizionario con i seguenti studenti e voti: studenti = {"Mario": [8, 9, 8], "Luca": [7, 7, 7], "Anna": [9, 10, 8]}.
3. Per ogni studente, calcola la media dei voti e stampala.

Nota: Puoi usare funzioni built-in come sum() per calcolare la somma degli elementi di una lista.

Nota: Per scorrere le chiavi di un dizionario, usa 'for chiave in dizionario:' e accedi al valore con 'dizionario[chiave]'.

Esempio: studenti["Mario"] restituisce la lista dei voti di Mario, ad esempio [8, 9, 8].

Esempio di ciclo for: 

```python
for nome in studenti: 
    print(nome, studenti[nome])
```

Esempio di output:
```
Mario: Media voti = 8.5
Luca: Media voti = 7.0
Anna: Media voti = 9.2
```