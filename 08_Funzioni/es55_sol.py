def filtra_partite_squadra(partite_lista: list[dict], squadra_nome: str) -> list[dict]:
    """Restituisce tutte le partite in cui la squadra ha giocato."""
    risultati = []
    for partita in partite_lista:
        if partita["squadra_casa"] == squadra_nome or partita["squadra_trasferta"] == squadra_nome:
            risultati.append(partita)
    return risultati


def calcola_gol_fatti(partite_lista: list[dict], squadra_nome: str) -> float:
    """Calcola la media dei gol fatti dalla squadra."""
    gol_totali = 0
    partite_giocate = 0
    
    for partita in partite_lista:
        if partita["squadra_casa"] == squadra_nome:
            gol_totali += partita["gol_casa"]
            partite_giocate += 1
        elif partita["squadra_trasferta"] == squadra_nome:
            gol_totali += partita["gol_trasferta"]
            partite_giocate += 1
    
    if partite_giocate == 0:
        return 0.0
    return gol_totali / partite_giocate


def calcola_gol_subiti(partite_lista: list[dict], squadra_nome: str) -> float:
    """Calcola la media dei gol subiti dalla squadra."""
    gol_totali = 0
    partite_giocate = 0
    
    for partita in partite_lista:
        if partita["squadra_casa"] == squadra_nome:
            gol_totali += partita["gol_trasferta"]
            partite_giocate += 1
        elif partita["squadra_trasferta"] == squadra_nome:
            gol_totali += partita["gol_casa"]
            partite_giocate += 1
    
    if partite_giocate == 0:
        return 0.0
    return gol_totali / partite_giocate


def conta_risultati(partite_lista: list[dict], squadra_nome: str) -> dict:
    """Conta vittorie, pareggi e sconfitte della squadra."""
    vittorie = 0
    pareggi = 0
    sconfitte = 0
    
    for partita in partite_lista:
        if partita["squadra_casa"] == squadra_nome:
            if partita["gol_casa"] > partita["gol_trasferta"]:
                vittorie += 1
            elif partita["gol_casa"] == partita["gol_trasferta"]:
                pareggi += 1
            else:
                sconfitte += 1
        elif partita["squadra_trasferta"] == squadra_nome:
            if partita["gol_trasferta"] > partita["gol_casa"]:
                vittorie += 1
            elif partita["gol_trasferta"] == partita["gol_casa"]:
                pareggi += 1
            else:
                sconfitte += 1
    
    return {"vittorie": vittorie, "pareggi": pareggi, "sconfitte": sconfitte}


def calcola_percentuale_vittorie(partite_lista: list[dict], squadra_nome: str) -> float:
    """Calcola la percentuale di vittorie della squadra."""
    risultati = conta_risultati(partite_lista, squadra_nome)
    partite_giocate = risultati["vittorie"] + risultati["pareggi"] + risultati["sconfitte"]
    
    if partite_giocate == 0:
        return 0.0
    return (risultati["vittorie"] / partite_giocate) * 100


def estrai_squadre_uniche(partite_lista: list[dict]) -> list[str]:
    """Estrae la lista di squadre uniche dal dataset."""
    squadre = []
    for partita in partite_lista:
        if partita["squadra_casa"] not in squadre:
            squadre.append(partita["squadra_casa"])
        if partita["squadra_trasferta"] not in squadre:
            squadre.append(partita["squadra_trasferta"])
    return squadre


def squadra_massimi_gol(partite_lista: list[dict], tipo: str) -> dict:
    """Trova la squadra con massimi gol fatti (tipo='fatti') o subiti (tipo='subiti')."""
    squadre = estrai_squadre_uniche(partite_lista)
    
    miglior_squadra = None
    massimo = -1
    
    for squadra in squadre:
        if tipo == "fatti":
            media = calcola_gol_fatti(partite_lista, squadra)
        else:  # tipo == "subiti"
            media = calcola_gol_subiti(partite_lista, squadra)
        
        if media > massimo:
            massimo = media
            miglior_squadra = squadra
    
    return {"squadra": miglior_squadra, "media": massimo}


def stampa_intestazione() -> None:
    """Stampa l'intestazione del report."""
    print("\n" + "=" * 70)
    print("ANALYZER PARTITE CALCIO".center(70))
    print("=" * 70 + "\n")


def stampa_partite(partite_lista: list[dict]) -> None:
    """Stampa tutte le partite in formato tabella."""
    print("TUTTE LE PARTITE")
    print("-" * 70)
    print(f"{'Data':<12} {'Casa':<20} {'Trasferta':<20} {'Risultato':<10}")
    print("-" * 70)
    
    for partita in partite_lista:
        risultato = f"{partita['gol_casa']}-{partita['gol_trasferta']}"
        print(
            f"{partita['data']:<12} "
            f"{partita['squadra_casa']:<20} "
            f"{partita['squadra_trasferta']:<20} "
            f"{risultato:<10}"
        )
    print()


def stampa_statistiche_squadre(partite_lista: list[dict], squadre_lista: list[str]) -> None:
    """Stampa le statistiche dettagliate per ogni squadra."""
    print("STATISTICHE SQUADRE")
    print("-" * 70)
    
    for squadra in squadre_lista:
        partite_squadra = filtra_partite_squadra(partite_lista, squadra)
        risultati = conta_risultati(partite_lista, squadra)
        gol_fatti = calcola_gol_fatti(partite_lista, squadra)
        gol_subiti = calcola_gol_subiti(partite_lista, squadra)
        perc_vittorie = calcola_percentuale_vittorie(partite_lista, squadra)
        
        print(f"\n{squadra}")
        print("-" * 70)
        print(f"Partite: {len(partite_squadra)}")
        print(
            f"Vittorie: {risultati['vittorie']} - "
            f"Pareggi: {risultati['pareggi']} - "
            f"Sconfitte: {risultati['sconfitte']}"
        )
        print(f"Gol fatti (media): {gol_fatti:.2f}")
        print(f"Gol subiti (media): {gol_subiti:.2f}")
        print(f"% Vittorie: {perc_vittorie:.2f}%")
    
    print()


def main() -> None:
    """Funzione principale che orchestra il report."""
    # Dati hardcoded
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
    
    # Estrai squadre uniche
    squadre = estrai_squadre_uniche(partite)
    
    # Orchestra il report
    stampa_intestazione()
    stampa_partite(partite)
    stampa_statistiche_squadre(partite, squadre)
    print("=" * 70)


# Avvio del programma
main()
