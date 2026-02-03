"""
ANALYZER PARTITE CALCIO - VERSIONE CON RICH
============================================

Per installare la libreria Rich:
  pip install rich

Oppure nel tuo ambiente virtuale:
  .venv/bin/pip install rich

Rich è una libreria Python per creare output nel terminale
con tabelle colorate, testo formattato e stili professionali.

Documentazione: https://rich.readthedocs.io/
"""

from rich.table import Table
from rich.console import Console
from rich.progress import Progress
from rich import box

# Istanza globale console di Rich
console = Console()


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


def get_colore_risultato(gol_casa: int, gol_trasferta: int, ruolo: str) -> str:
    """Restituisce il colore per il risultato e il ruolo della squadra."""
    if ruolo == "casa":
        if gol_casa > gol_trasferta:
            return "green"  # Vittoria
        elif gol_casa == gol_trasferta:
            return "yellow"  # Pareggio
        else:
            return "red"  # Sconfitta
    else:  # trasferta
        if gol_trasferta > gol_casa:
            return "green"  # Vittoria
        elif gol_trasferta == gol_casa:
            return "yellow"  # Pareggio
        else:
            return "red"  # Sconfitta


def stampa_intestazione() -> None:
    """Stampa l'intestazione del report con Rich."""
    console.print("\n", "⚽ ANALYZER PARTITE CALCIO ⚽".center(70), style="bold magenta")
    console.print()


def stampa_partite(partite_lista: list[dict]) -> None:
    """Stampa tutte le partite in una tabella Rich."""
    table = Table(title="TUTTE LE PARTITE", box=box.ROUNDED, show_header=True)
    
    table.add_column("Data", style="cyan")
    table.add_column("Casa", style="bold blue")
    table.add_column("Trasferta", style="bold blue")
    table.add_column("Risultato", style="bold yellow")
    
    for partita in partite_lista:
        risultato = f"{partita['gol_casa']}-{partita['gol_trasferta']}"
        colore_risultato = get_colore_risultato(
            partita['gol_casa'], 
            partita['gol_trasferta'], 
            "casa"
        )
        
        table.add_row(
            partita['data'],
            partita['squadra_casa'],
            partita['squadra_trasferta'],
            f"[{colore_risultato}]{risultato}[/{colore_risultato}]"
        )
    
    console.print(table)


def stampa_statistiche_squadre(partite_lista: list[dict], squadre_lista: list[str]) -> None:
    """Stampa le statistiche dettagliate per ogni squadra con Rich."""
    table = Table(title="STATISTICHE SQUADRE", box=box.DOUBLE, show_header=True)
    
    table.add_column("Squadra", style="bold cyan")
    table.add_column("Partite", style="white", justify="center")
    table.add_column("V-P-S", style="white", justify="center")
    table.add_column("Gol/Media", style="green", justify="center")
    table.add_column("% Vittorie", style="yellow", justify="center")
    table.add_column("Performance", style="magenta")
    
    for squadra in squadre_lista:
        partite_squadra = filtra_partite_squadra(partite_lista, squadra)
        risultati = conta_risultati(partite_lista, squadra)
        gol_fatti = calcola_gol_fatti(partite_lista, squadra)
        gol_subiti = calcola_gol_subiti(partite_lista, squadra)
        perc_vittorie = calcola_percentuale_vittorie(partite_lista, squadra)
        
        # Stringa V-P-S
        vps = f"{risultati['vittorie']}-{risultati['pareggi']}-{risultati['sconfitte']}"
        
        # Gol
        gol = f"F:{gol_fatti:.2f} S:{gol_subiti:.2f}"
        
        # Barra di performance
        riempimento = int(perc_vittorie / 10)
        barra = "█" * riempimento + "░" * (10 - riempimento)
        
        # Emoji in base alle vittorie
        if perc_vittorie >= 70:
            emoji = "🔥"
        elif perc_vittorie >= 50:
            emoji = "💪"
        else:
            emoji = "😢"
        
        table.add_row(
            f"{emoji} {squadra}",
            str(len(partite_squadra)),
            vps,
            gol,
            f"{perc_vittorie:.1f}%",
            barra
        )
    
    console.print(table)


def stampa_podio(partite_lista: list[dict], squadre_lista: list[str]) -> None:
    """Stampa il podio con le migliori squadre."""
    # Calcola ranking per percentuale vittorie (come lista di dizionari)
    ranking = []
    for squadra in squadre_lista:
        perc = calcola_percentuale_vittorie(partite_lista, squadra)
        ranking.append({"squadra": squadra, "percentuale": perc})
    
    # Ordina dal più alto al più basso
    ranking.sort(key=lambda x: x["percentuale"], reverse=True)
    
    # Prendi i primi 3 (il [:3] prende da 0 a 2, o meno se ci sono meno di 3 squadre)
    migliori = ranking[:3]
    
    console.print("\n📊 PODIO - MIGLIORI SQUADRE", style="bold yellow")
    
    medaglie = ["🥇", "🥈", "🥉"]
    for i, elem in enumerate(migliori):
        console.print(
            f"  {medaglie[i]} {elem['squadra']:<15} - {elem['percentuale']:.1f}% vittorie",
            style="bold" if i == 0 else ""
        )


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
    stampa_podio(partite, squadre)
    
    console.print()


# Avvio del programma
if __name__ == "__main__":
    main()
