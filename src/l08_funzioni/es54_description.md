# Esercizio 54: Tracker Film Visti - Statistiche e Ricerca

## Obiettivo
Gestire un tracker di film visti con analisi dei dati usando l'approccio top-down. I dati sono forniti hardcoded per velocità.

## Dati forniti
Una lista di dizionari con struttura:
```python
film = [
    {"titolo": "The Shawshank Redemption", "genere": "Drammatico", "anno": 1994, "voto": 9},
    {"titolo": "Inception", "genere": "Fantascienza", "anno": 2010, "voto": 8},
    {"titolo": "Pulp Fiction", "genere": "Thriller", "anno": 1994, "voto": 8},
    {"titolo": "Interstellar", "genere": "Fantascienza", "anno": 2014, "voto": 8},
    {"titolo": "Parasite", "genere": "Thriller", "anno": 2019, "voto": 9},
    {"titolo": "The Dark Knight", "genere": "Azione", "anno": 2008, "voto": 9},
    {"titolo": "Forrest Gump", "genere": "Drammatico", "anno": 1994, "voto": 8},
    {"titolo": "Oppenheimer", "genere": "Drammatico", "anno": 2023, "voto": 8},
]
```

## Istruzioni

1. **Definire `calcola_voto_medio(film_lista)`**: Accetta una lista di film e restituisce la media dei voti.

2. **Definire `trova_film_migliore(film_lista)`**: Accetta una lista di film e restituisce il **dizionario** del film con il voto più alto.

3. **Definire `film_per_genere(film_lista, genere_ricerca)`**: Accetta la lista film e una stringa con il genere da cercare. Restituisce una lista con tutti i film di quel genere.

4. **Definire `conta_film_per_anno(film_lista)`**: Accetta la lista e restituisce un dizionario con il conteggio:
   ```python
   {"1994": 3, "2008": 1, "2010": 1, ...}
   ```
   Le chiavi sono stringhe (anni).

5. **Definire `stampa_intestazione()`**: Stampa l'intestazione del report.

6. **Definire `stampa_film(film_lista)`**: Stampa tutti i film in formato tabella:
   ```
   Titolo                        Genere        Anno  Voto
   The Shawshank Redemption      Drammatico    1994  9
   Inception                     Fantascienza  2010  8
   ...
   ```

7. **Definire `stampa_statistiche(film_lista)`**: Calcola e stampa:
   - Numero totale film visti
   - Voto medio
   - Film con voto più alto (titolo + voto)
   - Generi disponibili (lista unica)

8. **Definire `stampa_film_per_genere(film_lista)`**: Per ogni genere diverso, stampa:
   ```
   Drammatico (3 film):
     - The Shawshank Redemption (1994, voto 9)
     - Forrest Gump (1994, voto 8)
     - Oppenheimer (2023, voto 8)
   ```

9. **Definire `main()`**: Orchestra il programma:
   - Definisce `film` (dati hardcoded)
   - Stampa intestazione
   - Stampa lista completa film
   - Stampa statistiche generali
   - Stampa film raggruppati per genere

## Suggerimenti
- Non serve importare nulla
- Usa cicli for semplici per filtrare e contare
- Formatta stringhe con f-string
- Per generi unici: cicla film e accumula in lista se non esiste già
- Ogni funzione ha un compito singolo
- Nel main orchestri tutto in ordine logico

## Esempio di output atteso (parziale)
```
================================================================
                    TRACKER FILM VISTI
================================================================

TUTTI I FILM
----------------------------------------------------------------
Titolo                        Genere        Anno  Voto
----------------------------------------------------------------
The Shawshank Redemption      Drammatico    1994  9
Inception                     Fantascienza  2010  8
...

STATISTICHE GENERALI
----------------------------------------------------------------
Film visti: 8
Voto medio: 8.38
Film migliore: The Dark Knight (9)
Generi: Drammatico, Fantascienza, Thriller, Azione

FILM PER GENERE
----------------------------------------------------------------
Drammatico (3 film):
  - The Shawshank Redemption (1994, voto 9)
  - Forrest Gump (1994, voto 8)
  - Oppenheimer (2023, voto 8)

Fantascienza (2 film):
  - Inception (2010, voto 8)
  - Interstellar (2014, voto 8)

...
```

## Spiegazione Sintassi

### 1. **Filtraggio con ciclo e lista**
```python
def film_per_genere(film_lista, genere_ricerca):
    risultati = []
    for film in film_lista:
        if film["genere"] == genere_ricerca:
            risultati.append(film)
    return risultati
```
- Crea una lista vuota
- Cicla tutti i film
- Se il genere corrisponde, aggiunge a `risultati`
- Restituisce la lista filtrata

### 2. **Generi unici (senza duplicati)**
```python
generi = []
for film in film_lista:
    if film["genere"] not in generi:
        generi.append(film["genere"])
```
- Controlla se il genere è già nella lista
- Se no, lo aggiunge
- Risultato: lista senza duplicati

### 3. **Conteggio in dizionario**
```python
conteggi = {}
for film in film_lista:
    anno_str = str(film["anno"])
    if anno_str not in conteggi:
        conteggi[anno_str] = 0
    conteggi[anno_str] += 1
```
- Crea dizionario vuoto
- Per ogni film, crea chiave se non esiste
- Incrementa il conteggio
