# Esercizio 56: Scrittura e Lettura di un File di Testo Semplice

## Obiettivo
Creare un programma che scriva una lista di stringhe su un file e poi lo rilegga, stampando il contenuto.

## Dati forniti
Una lista di frasi hardcoded:
```python
frasi = ["Ciao mondo", "Python è divertente", "File handling"]
```

## Istruzioni

1. **Definire `scrivi_file(frasi, nome_file)`**: Accetta una lista di stringhe e un nome file. Scrive ogni frase su una riga separata nel file.

2. **Definire `leggi_file(nome_file)`**: Accetta un nome file e restituisce una lista con le righe lette (senza newline).

3. **Definire `main()`**: 
   - Definisce `frasi` (dati hardcoded)
   - Chiama `scrivi_file` per salvare su "esercizio56.txt"
   - Chiama `leggi_file` per leggere e stampare il contenuto

## Suggerimenti
- Usa `with open` per aprire i file in modalità 'w' per scrittura e 'r' per lettura
- Per scrivere: `file.write(frase + "\n")`
- Per leggere: usa un ciclo `for line in file:` e `.strip()` per rimuovere newline
- Gestisci encoding UTF-8

## Esempio di output atteso
```
Contenuto del file:
Ciao mondo
Python è divertente
File handling
```