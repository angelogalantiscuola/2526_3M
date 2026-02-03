# Esercizio 55: Analyzer Partite Calcio - Statistiche Squadre

## Obiettivo
Analizzare statistiche di calcio con approccio top-down. I dati sono forniti hardcoded per velocità.

## Dati forniti
Una lista di dizionari con struttura:
```python
partite = [
    {"data": "2024-01-15", "squadra_casa": "Milan", "squadra_trasferta": "Juventus", "gol_casa": 2, "gol_trasferta": 1},
    {"data": "2024-01-16", "squadra_casa": "Inter", "squadra_trasferta": "Napoli", "gol_casa": 3, "gol_trasferta": 2},
    {"data": "2024-01-17", "squadra_casa": "Juventus", "squadra_trasferta": "Lazio", "gol_casa": 1, "gol_trasferta": 1},
    {"data": "2024-01-18", "squadra_casa": "Milan", "squadra_trasferta": "Roma", "gol_casa": 2, "gol_trasferta": 0},
    {"data": "2024-01-19", "squadra_casa": "Napoli", "squadra_trasferta": "Inter", "gol_casa": 1, "gol_trasferta": 2},
    {"data": "2024-01-20", "squadra_casa": "Lazio", "squadra_trasferta": "Milan", "gol_casa": 0, "gol_trasferta": 3},
    {"data": "2024-01-21", "squadra_casa": "Roma", "squadra_trasferta": "Napoli", "gol_casa": 2, "gol_trasferta": 1},
    {"data": "2024-01-22", "squadra_casa": "Juventus", "squadra_trasferta": "Inter", "gol_casa": 1, "gol_trasferta": 2},
]
```

## Istruzioni

1. **Definire `filtra_partite_squadra(partite_lista, squadra_nome)`**: Accetta la lista partite e una squadra. Restituisce una lista con tutte le partite in cui la squadra ha giocato (casa o trasferta).

2. **Definire `calcola_gol_fatti(partite_lista, squadra_nome)`**: Accetta lista partite e squadra. Calcola la media dei gol fatti dalla squadra.

3. **Definire `calcola_gol_subiti(partite_lista, squadra_nome)`**: Accetta lista partite e squadra. Calcola la media dei gol subiti.

4. **Definire `conta_risultati(partite_lista, squadra_nome)`**: Accetta lista partite e squadra. Restituisce un dizionario con:
   ```python
   {"vittorie": 2, "pareggi": 1, "sconfitte": 1}
   ```

5. **Definire `calcola_percentuale_vittorie(partite_lista, squadra_nome)`**: Accetta lista partite e squadra. Restituisce percentuale vittorie (0-100).

6. **Definire `estrai_squadre_uniche(partite_lista)`**: Estrae la lista di squadre uniche dal dataset.

7. **Definire `squadra_massimi_gol(partite_lista, tipo)`**: Accetta lista e tipo ("fatti" o "subiti"). Restituisce il dizionario della squadra con statistica migliore.
   
8. **Definire `stampa_intestazione()`**: Stampa l'intestazione del report.

9. **Definire `stampa_partite(partite_lista)`**: Stampa tutte le partite in formato tabella:
   ```
   Data         Casa                Trasferta            Risultato
   2024-01-15   Milan               Juventus             2-1
   2024-01-16   Inter               Napoli               3-2
   ```

10. **Definire `stampa_statistiche_squadre(partite_lista, squadre_lista)`**: Per ogni squadra, stampa:
    ```
    Milan
    --------
    Partite: 3
    Vittorie: 2 - Pareggi: 0 - Sconfitte: 1
    Gol fatti (media): 2.33
    Gol subiti (media): 1.00
    % Vittorie: 66.67%
    ```

11. **Definire `main()`**: Orchestra il programma:
    - Definisce `partite` (dati hardcoded)
    - Estrae squadre uniche
    - Stampa intestazione
    - Stampa lista partite
    - Stampa statistiche per ogni squadra

## Suggerimenti
- Non serve importare nulla
- Usa cicli for per filtrare e contare
- Per discernere se gol_casa o gol_trasferta: controlla se `squadra_nome == partita["squadra_casa"]`
- Formatta stringhe con f-string
- Per squadre uniche: cicla partite e accumula se non esiste già
- Ogni funzione ha un compito singolo

## Esempio di output atteso (parziale)
```
================================================================
                  ANALYZER PARTITE CALCIO
================================================================

TUTTE LE PARTITE
----------------------------------------------------------------
Data         Casa                 Trasferta             Risultato
----------------------------------------------------------------
2024-01-15   Milan                Juventus              2-1
2024-01-16   Inter                Napoli                3-2
...

STATISTICHE SQUADRE
----------------------------------------------------------------

Milan
--------
Partite: 3
Vittorie: 2 - Pareggi: 0 - Sconfitte: 1
Gol fatti (media): 2.33
Gol subiti (media): 1.00
% Vittorie: 66.67%

Juventus
--------
Partite: 2
Vittorie: 0 - Pareggi: 1 - Sconfitte: 1
Gol fatti (media): 1.00
Gol subiti (media): 1.50
% Vittorie: 0.00%

...
================================================================
```
