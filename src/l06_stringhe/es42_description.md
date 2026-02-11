# Esercizio 43: Analisi di Testo con Stringhe e Liste

Scrivi un programma che analizzi un testo fornito dall'utente.

- Leggi un testo come stringa.
- Dividi il testo in parole usando il metodo `split()`.
- Per ciascuna parola, conta le vocali (a, e, i, o, u, sia maiuscole che minuscole) usando metodi stringa come `lower()` e `count()`.
- Usa un dizionario per memorizzare il conteggio delle vocali per ogni parola.
- Trova la parola con il maggior numero di vocali.
- Se ci sono più parole con lo stesso massimo, scegli la prima.

Stampa il dizionario dei conteggi e la parola con più vocali.

**Esempio di output:**
```
Testo: "Ciao mondo"
Conteggi vocali: {'Ciao': 3, 'mondo': 2}
Parola con più vocali: Ciao (3 vocali)
```