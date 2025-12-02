# Esercizio 38: Liste e Dizionari Annidati

Scrivi un programma Python che:

1. Crea una lista di dizionari, dove ogni dizionario rappresenta un'azienda con chiavi "nome", "settore", e "dipendenti". La chiave "dipendenti" è una lista di dizionari, ciascuno rappresentante un dipendente con chiavi "nome", "età", "ruolo".
2. Aggiungi almeno 2 aziende con i loro dipendenti.
3. Per ogni azienda, stampa il nome dell'azienda, il settore, e i nomi e ruoli dei suoi dipendenti.

```python
    aziende = [
        {
            "nome": "TechCorp",
            "settore": "Tecnologia",
            "dipendenti": [
                {"nome": "Mario", "età": 30, "ruolo": "Sviluppatore"},
                {"nome": "Luca", "età": 25, "ruolo": "Designer"},
            ],
        },
        {
            "nome": "FoodInc",
            "settore": "Alimentare",
            "dipendenti": [
                {"nome": "Anna", "età": 35, "ruolo": "Manager"},
                {"nome": "Giovanni", "età": 28, "ruolo": "Cuoco"},
            ],
        },
    ]
```

Esempio di output:
```
Azienda: TechCorp, Settore: Tecnologia
Dipendenti: Mario (Sviluppatore), Luca (Designer)
Azienda: FoodInc, Settore: Alimentare
Dipendenti: Anna (Manager), Giovanni (Cuoco)
```