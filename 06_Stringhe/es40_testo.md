# Esercizio 40: Formattazione e metodi con dizionari e cicli

Scrivi un programma che utilizzi il seguente dizionario per memorizzare dati di prodotti:

```python
prodotti = {
    "prodotto1": {"nome": "Mela", "prezzo": 1.50, "quantita": 10},
    "prodotto2": {"nome": "Banana", "prezzo": 2.00, "quantita": 5},
    "prodotto3": {"nome": "Arancia", "prezzo": 1.20, "quantita": 8}
}
```

Per ciascun prodotto, esegui le seguenti operazioni usando cicli:

- **Metodi stringa**: Verifica se il nome inizia con 'M' e conta le occorrenze di 'a'.
- **Formattazione**: Calcola il totale con possibile sconto (10% se totale > 10 €) e formatta con 2 decimali.

Stampa i risultati per ogni prodotto.

**Esempio di output:**
Prodotto: Mela, Totale: 13.50 € (sconto 10%), Inizia con 'M': True, Conteggio 'a': 1