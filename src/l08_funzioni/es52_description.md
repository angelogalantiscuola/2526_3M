# Esercizio 52: Calcolatore BMI con approccio top-down

## Obiettivo
Creare un programma per calcolare l'Indice di Massa Corporea (BMI) e classificare il risultato usando l'approccio top-down con molteplici funzioni specializzate.

## Formula BMI
BMI = peso (kg) / (altezza (m))²

## Categorie BMI
- < 18.5: Sottopeso
- 18.5 - 24.9: Peso normale
- 25.0 - 29.9: Sovrappeso
- ≥ 30.0: Obeso

## Approccio top-down
Decomporre il problema principale in sottoproblemi indipendenti:
- Acquisire i dati dell'utente (peso e altezza)
- Validare i dati inseriti
- Calcolare il BMI
- Classificare il risultato in categoria
- Visualizzare il risultato in modo leggibile
- Gestire il menu principale

## Istruzioni

1. **Definire `chiedi_peso()`**: Chiede all'utente il peso in kg. Valida che sia > 0. Se non valido, chiede di nuovo. Restituisce il peso come float.

2. **Definire `chiedi_altezza()`**: Chiede all'utente l'altezza in metri. Valida che sia > 0. Se non valido, chiede di nuovo. Restituisce l'altezza come float.

3. **Definire `calcola_bmi(peso, altezza)`**: Accetta peso (kg) e altezza (m), calcola e restituisce il BMI come float.

4. **Definire `classifica_bmi(bmi)`**: Accetta il valore BMI e restituisce una stringa con la categoria: "Sottopeso", "Peso normale", "Sovrappeso" o "Obeso".

5. **Definire `get_colore_categoria(bmi)`**: Accetta il BMI e restituisce un'emoji per visualizzare la categoria:
   - BMI < 18.5: "🔵 Sottopeso"
   - BMI 18.5-24.9: "🟢 Peso normale"
   - BMI 25.0-29.9: "🟡 Sovrappeso"
   - BMI ≥ 30.0: "🔴 Obeso"

6. **Definire `stampa_risultato(peso, altezza, bmi, categoria)`**: Stampa un risultato formattato con:
   - Peso: X.X kg
   - Altezza: X.XX m
   - BMI: X.X
   - Categoria con emoji

7. **Definire `stampa_menu()`**: Stampa il menu con opzioni:
   - "1. Calcola BMI"
   - "2. Esci"

8. **Definire `main()`**: Orchestra il programma:
   - Mostra il menu in un ciclo while
   - Se scelta 1: chiama `chiedi_peso()` e `chiedi_altezza()`, calcola BMI e categoria, stampa il risultato
   - Se scelta 2: esce dal ciclo
   - Gestisce scelte non valide

## Suggerimenti
- Usa try-except per convertire gli input a float in `chiedi_peso()` e `chiedi_altezza()`
- La formula: BMI = peso / (altezza * altezza)
- Usa if-elif-else per classificare il BMI
- Formatta il BMI con 1 decimale nella stampa (f"{bmi:.1f}")
- Ogni funzione ha un compito specifico (single responsibility)
