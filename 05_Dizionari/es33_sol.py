def main() -> None:
    colori = {}
    colori["rosso"] = "#FF0000"
    colori["blu"] = "#0000FF"
    colori["verde"] = "#00FF00"

    colore_da_cercare = input("Inserisci un colore da verificare: ")
    if colore_da_cercare in colori.keys():
        print("Colore presente")
    else:
        print("Colore non trovato")


if __name__ == "__main__":
    main()
