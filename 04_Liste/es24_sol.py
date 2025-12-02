def main():
    n = int(input("Inserisci il numero di righe (n): "))
    m = int(input("Inserisci il numero di colonne (m): "))

    if n <= 0 or m <= 0:
        print("Errore: n e m devono essere positivi.")
        return

    # n = 2, m = 3
    for _ in range(n):  # Itera sulle righe
        for _ in range(m):  # Itera sulle colonne
            print("1", end=" ")  # Stampa "1" con uno spazio
        print()


if __name__ == "__main__":
    main()
