# Esercizio 58: Gestione di un File JSON con Dati Studenti

## Obiettivo
Salvare e caricare una lista di studenti (dizionari) in formato JSON, calcolando la media dei voti.

## Dati forniti
Una lista di studenti hardcoded:
```python
studenti = [
    {"nome": "Alice", "voto": 8},
    {"nome": "Bob", "voto": 7},
    {"nome": "Carlo", "voto": 9}
]
```

## Istruzioni

1. **Definire `salva_studenti(studenti, nome_file)`**: Accetta una lista di dizionari e un nome file. Salva la lista in JSON con indentazione.

2. **Definire `carica_studenti(nome_file)`**: Accetta un nome file e restituisce la lista di dizionari caricata da JSON.

3. **Definire `calcola_media(studenti)`**: Accetta la lista e restituisce la media dei voti (float).

4. **Definire `main()`**: 
   - Definisce `studenti` (dati hardcoded)
   - Chiama `salva_studenti` su "studenti.json"
   - Chiama `carica_studenti` e `calcola_media`
   - Stampa la lista caricata e la media

## Suggerimenti
- Importa `json`
- Usa `json.dump` per salvare (con `indent=4`)
- Usa `json.load` per caricare
- Gestisci `FileNotFoundError` in caricamento
- Per media: somma voti / len(studenti)

## Esempio di output atteso
```
File 'studenti.json' salvato con successo.
Studenti caricati: [{'nome': 'Alice', 'voto': 8}, {'nome': 'Bob', 'voto': 7}, {'nome': 'Carlo', 'voto': 9}]
Media voti: 8.0
```