# Esercizio 53: Gestione Voti con Statistiche Semplici

## Obiettivo
Analizzare voti di studenti e calcolare statistiche di base (media, min, max) usando l'approccio top-down con funzioni specializzate. I dati sono forniti hardcoded per velocità.

## Dati forniti
Una lista di dizionari con struttura:
```python
voti = [
    {"nome": "Alice", "voti": [8.5, 7.8, 9.0, 8.2]},
    {"nome": "Bob", "voti": [6.5, 7.0, 6.8, 7.2]},
    {"nome": "Charlie", "voti": [9.5, 9.2, 9.8, 9.0]},
    {"nome": "Diana", "voti": [7.0, 8.5, 7.5, 8.0]},
    {"nome": "Eve", "voti": [5.5, 6.0, 5.8, 6.2]},
]
```

## Approccio top-down
Decomporre l'analisi in funzioni specializzate per ogni calcolo.

## Istruzioni

1. **Definire `calcola_media(voti_lista)`**: Accetta una lista di voti e restituisce la media come float.

2. **Definire `analizza_studente(nome, voti_lista)`**: Accetta nome e lista voti dello studente. Restituisce un dizionario con:
   - "nome", "media", "min", "max"
   
   All'interno usa `min()` e `max()` direttamente.

3. **Definire `stampa_intestazione()`**: Stampa un'intestazione semplice per il report.

4. **Definire `stampa_studenti(dati_analizzati)`**: Stampa una riga per ogni studente con formato tabella:
   ```
   Nome       Media  Min   Max
   Alice      8.38   7.8   9.0
   Bob        6.88   6.5   7.2
   ...
   ```

5. **Definire `stampa_media_classe(dati_studenti)`**: Calcola la media di tutte le medie e stampa:
   ```
   Media classe: 7.94
   ```

6. **Definire `main()`**: Orchestra il programma:
   - Definisce `voti` (dati hardcoded)
   - Stampa intestazione
   - Analizza ogni studente in un ciclo
   - Stampa i risultati
   - Stampa la media della classe

## Suggerimenti
- Non serve importare nulla
- Usa cicli for semplici per analizzare e stampare
- Formatta i float con `.2f`
- Ogni funzione ha un compito singolo
- Nel main: crea lista `dati_analizzati` con ciclo, poi stampa

## Esempio di output atteso
```
============================================================
                 REPORT VOTI - CLASSE
============================================================

STUDENTI
------------------------------------------------------------
Nome            Media        Min          Max
------------------------------------------------------------
Alice           8.38         7.80         9.00
Bob             6.88         6.50         7.20
Charlie         9.38         9.20         9.80
Diana           7.75         7.00         8.50
Eve             5.88         5.50         6.20

Media classe: 7.74

============================================================
```

## Spiegazione Sintassi

### 1. **Lista di dizionari**
```python
voti = [
    {"nome": "Alice", "voti": [8.5, 7.8, 9.0, 8.2]},
]
```
- `voti[0]["nome"]` → `"Alice"`
- `voti[0]["voti"]` → `[8.5, 7.8, 9.0, 8.2]`

### 2. **Ciclo su lista di dizionari**
```python
for studente in voti:
    print(studente["nome"])  # Stampa: Alice, Bob, Charlie, ...
```

### 3. **Min e Max**
```python
min([8.5, 7.8, 9.0, 8.2])  # Restituisce 7.8
max([8.5, 7.8, 9.0, 8.2])  # Restituisce 9.0
```

### 4. **F-string con formattazione**
```python
print(f"{'Nome':<15} {'Media':<12.2f}")
```
- `<15` = allineamento sinistra, 15 caratteri
- `.2f` = numero float con 2 decimali
