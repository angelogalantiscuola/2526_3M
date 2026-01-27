def calcola_media(voti_lista: list[float]) -> float:
    """Calcola la media dei voti."""
    return sum(voti_lista) / len(voti_lista)


def analizza_studente(nome: str, voti_lista: list[float]) -> dict:
    """Analizza uno studente e restituisce le statistiche base."""
    return {
        "nome": nome,
        "media": calcola_media(voti_lista),
        "min": min(voti_lista),
        "max": max(voti_lista),
    }


def stampa_intestazione() -> None:
    """Stampa l'intestazione del report."""
    print("\n" + "=" * 60)
    print("REPORT VOTI - CLASSE".center(60))
    print("=" * 60 + "\n")


def stampa_studenti(dati_analizzati: list[dict]) -> None:
    """Stampa il report degli studenti in formato tabella."""
    print("STUDENTI")
    print("-" * 60)
    print(f"{'Nome':<15} {'Media':<12} {'Min':<12} {'Max':<12}")
    print("-" * 60)
    for studente in dati_analizzati:
        print(
            f"{studente['nome']:<15} "
            f"{studente['media']:<12.2f} "
            f"{studente['min']:<12.2f} "
            f"{studente['max']:<12.2f}"
        )
    print()


def stampa_media_classe(dati_studenti: list[dict]) -> None:
    """Calcola e stampa la media della classe."""
    somma_medie = 0.0
    for studente in dati_studenti:
        somma_medie += studente["media"]
    media_classe = somma_medie / len(dati_studenti)
    print(f"Media classe: {media_classe:.2f}")
    print()


def main() -> None:
    """Funzione principale che orchestra il report."""
    # Dati hardcoded
    voti = [
        {"nome": "Alice", "voti": [8.5, 7.8, 9.0, 8.2]},
        {"nome": "Bob", "voti": [6.5, 7.0, 6.8, 7.2]},
        {"nome": "Charlie", "voti": [9.5, 9.2, 9.8, 9.0]},
        {"nome": "Diana", "voti": [7.0, 8.5, 7.5, 8.0]},
        {"nome": "Eve", "voti": [5.5, 6.0, 5.8, 6.2]},
    ]

    # Analizza ogni studente
    dati_analizzati = []
    for studente in voti:
        dati = analizza_studente(studente["nome"], studente["voti"])
        dati_analizzati.append(dati)

    # Stampa il report
    stampa_intestazione()
    stampa_studenti(dati_analizzati)
    stampa_media_classe(dati_analizzati)
    print("=" * 60)


# Avvio del programma
main()


