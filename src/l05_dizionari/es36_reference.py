def main() -> None:
    punteggi = {"Mario": 10, "Luca": 8}

    nome = input("Inserisci il nome: ")
    nuovo_punteggio = int(input("Inserisci il nuovo punteggio: "))

    if nome in punteggi:
        punteggi[nome] = nuovo_punteggio
    else:
        punteggi[nome] = nuovo_punteggio

    print("Dizionario aggiornato:")
    for nome, punteggio in punteggi.items():
        print(f"{nome}: {punteggio}")


if __name__ == "__main__":
    main()
