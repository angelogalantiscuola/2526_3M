def main() -> None:
    prodotti = {"mela": 1.5, "banana": 2.0, "arancia": 1.8}

    conteggio = 0
    for prezzo in prodotti.values():
        if prezzo > 1.7:
            conteggio += 1

    print(f"Numero di prodotti che costano più di 1.7 euro: {conteggio}")


if __name__ == "__main__":
    main()
