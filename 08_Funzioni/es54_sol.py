def calcola_voto_medio(film_lista: list[dict]) -> float:
    """Calcola il voto medio dei film."""
    somma_voti = 0.0
    for film in film_lista:
        somma_voti += film["voto"]
    return somma_voti / len(film_lista)


def trova_film_migliore(film_lista: list[dict]) -> dict:
    """Trova e restituisce il film con il voto più alto."""
    migliore = film_lista[0]
    for film in film_lista:
        if film["voto"] > migliore["voto"]:
            migliore = film
    return migliore


def film_per_genere(film_lista: list[dict], genere_ricerca: str) -> list[dict]:
    """Restituisce la lista di film di un genere specifico."""
    risultati = []
    for film in film_lista:
        if film["genere"] == genere_ricerca:
            risultati.append(film)
    return risultati


def genera_generi_unici(film_lista: list[dict]) -> list[str]:
    """Restituisce una lista di generi unici (senza duplicati)."""
    generi = []
    for film in film_lista:
        if film["genere"] not in generi:
            generi.append(film["genere"])
    return generi


def stampa_intestazione() -> None:
    """Stampa l'intestazione del report."""
    print("\n" + "=" * 70)
    print("TRACKER FILM VISTI".center(70))
    print("=" * 70 + "\n")


def stampa_film(film_lista: list[dict]) -> None:
    """Stampa tutti i film in formato tabella."""
    print("TUTTI I FILM")
    print("-" * 70)
    print(f"{'Titolo':<30} {'Genere':<15} {'Anno':<6} {'Voto':<5}")
    print("-" * 70)
    for film in film_lista:
        print(
            f"{film['titolo']:<30} "
            f"{film['genere']:<15} "
            f"{film['anno']:<6} "
            f"{film['voto']:<5}"
        )
    print()


def stampa_statistiche(film_lista: list[dict]) -> None:
    """Stampa le statistiche generali del tracker."""
    voto_medio = calcola_voto_medio(film_lista)
    film_migliore = trova_film_migliore(film_lista)
    generi = genera_generi_unici(film_lista)

    print("STATISTICHE GENERALI")
    print("-" * 70)
    print(f"Film visti: {len(film_lista)}")
    print(f"Voto medio: {voto_medio:.2f}")
    print(f"Film migliore: {film_migliore['titolo']} ({film_migliore['voto']})")

    # Stampa generi separati da virgola
    generi_str = ", ".join(generi)
    print(f"Generi: {generi_str}")
    print()


def stampa_film_per_genere(film_lista: list[dict]) -> None:
    """Stampa i film raggruppati per genere."""
    generi = genera_generi_unici(film_lista)

    print("FILM PER GENERE")
    print("-" * 70)
    for genere in generi:
        film_genere = film_per_genere(film_lista, genere)
        print(f"{genere} ({len(film_genere)} film):")
        for film in film_genere:
            print(f"  - {film['titolo']} ({film['anno']}, voto {film['voto']})")
        print()


def main() -> None:
    """Funzione principale che orchestra il report."""
    # Dati hardcoded
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

    # Orchestra il report
    stampa_intestazione()
    stampa_film(film)
    stampa_statistiche(film)
    stampa_film_per_genere(film)
    print("=" * 70)


# Avvio del programma
main()
