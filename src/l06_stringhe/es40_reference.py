# Esercizio 40: Formattazione e metodi con dizionari e cicli
# Usa un dizionario per memorizzare dati di prodotti (nome, prezzo, quantità).
# Per ciascun prodotto, usa metodi di stringa per verificare e contare caratteri.
# Formatta l'output con decimali.
# Applica sconti basati su condizioni e cicli.

prodotti = {
    "prodotto1": {"nome": "Mela", "prezzo": 1.50, "quantita": 10},
    "prodotto2": {"nome": "Banana", "prezzo": 2.00, "quantita": 5},
    "prodotto3": {"nome": "Arancia", "prezzo": 1.20, "quantita": 8},
}

for chiave, dati in prodotti.items():
    nome = dati["nome"]
    totale = dati["prezzo"] * dati["quantita"]
    sconto = 0.1 if totale > 10 else 0
    totale_scontato = totale * (1 - sconto)

    # Metodi stringa
    inizia_con_m = nome.startswith("M")
    conteggio_a = nome.count("a")

    print(
        f"Prodotto: {nome}, Totale: {totale_scontato:.2f} € (sconto {sconto * 100:.0f}%), Inizia con 'M': {inizia_con_m}, Conteggio 'a': {conteggio_a}"
    )
