def main() -> None:
    giocatori = {"Mario": 85, "Luca": 92, "Anna": 78, "Giulia": 95}

    max_punteggio = 0
    vincitore = ""

    for nome in giocatori:
        punteggio = giocatori[nome]
        if punteggio > max_punteggio:
            max_punteggio = punteggio
            vincitore = nome

    print(
        f"Il giocatore con il punteggio più alto è {vincitore} con {max_punteggio} punti."
    )


if __name__ == "__main__":
    main()
