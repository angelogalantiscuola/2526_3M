# Esercizio Integrativo: Gioco RPG Semplice

## Obiettivo
Creare un programma Python per un semplice gioco RPG utilizzando liste, dizionari, stringhe, cicli, condizioni e input/output. Il programma deve permettere al giocatore di esplorare, combattere mostri, gestire l'inventario e visualizzare statistiche, senza utilizzare funzioni personalizzate.

## Strutture Dati
- **Personaggio**: Un dizionario con chiavi "nome" (stringa), "livello" (intero), "hp" (intero), "attacco" (intero).
- **Inventario**: Una lista di dizionari, ognuno con chiavi "nome" (stringa), "tipo" (stringa), "valore" (intero), "usato" (booleano).
- **Oggetti Possibili**: Una lista predefinita di dizionari per oggetti casuali.

Inizializzazione:
```python
personaggio = {"nome": "Eroe", "livello": 1, "hp": 100, "attacco": 10}
inventario = []

oggetti_possibili = [
    {"nome": "Spada", "tipo": "arma", "valore": 20, "usato": False},
    {"nome": "Pozione", "tipo": "cura", "valore": 30, "usato": False},
    {"nome": "Arco", "tipo": "arma", "valore": 15, "usato": False},
    {"nome": "Scudo", "tipo": "difesa", "valore": 10, "usato": False},
    {"nome": "Anello", "tipo": "magia", "valore": 25, "usato": False},
]
```

## Istruzioni
1. Utilizza il modulo `random` per scegliere oggetti casuali durante l'esplorazione (usando `random.choice()`) e per generare HP casuali dei mostri (usando `random.randint(50, 100)`).
2. Inizia con il personaggio e inventario come sopra.
3. Mostra un menu con opzioni numerate (usando un ciclo while per ripetere fino a scelta di uscita):
   - 1: Esplora (aggiungi un oggetto casuale all'inventario da `oggetti_possibili`).
   - 2: Combatti (scegli un oggetto dall'inventario per combattere un mostro casuale; se vinci, sali di livello; se perdi HP, potresti morire).
   - 3: Inventario (visualizza tutti gli oggetti con nome, tipo, valore, usato).
   - 4: Statistiche (mostra statistiche del personaggio e inventario: totale oggetti).
   - 5: Esci.
4. Gestisci input invalidi con messaggi di errore.
5. Usa cicli for per iterare su liste e dizionari, ciclo while per il menu principale con continue per saltare iterazioni e break per uscire, condizioni if/elif/else per il menu e la logica, e metodi stringa se necessario.

## Esempio
**Menu:**  
1. Esplora  
2. Combatti  
3. Inventario  
4. Statistiche  
5. Esci  

**Scelta: 1**  
Hai trovato: Spada (arma, valore: 20)  

**Scelta: 3**  
Inventario:  
- Nome: Spada, Tipo: arma, Valore: 20, Usato: False  

**Scelta: 4**  
Nome: Eroe, Livello: 1, HP: 100, Attacco: 10  
Totale oggetti: 1  

Questo esercizio integra input/output per interazione, condizioni per validazione e menu, cicli per menu e iterazioni, liste per inventario, dizionari per personaggio e oggetti, stringhe per output, e il modulo random per casualità.