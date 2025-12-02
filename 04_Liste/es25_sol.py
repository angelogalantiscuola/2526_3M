def main():
    n = int(input("Inserisci il numero di righe (n): "))
    m = int(input("Inserisci il numero di colonne (m): "))

    if n <= 0 or m <= 0:
        print("Errore: n e m devono essere positivi.")
        return

    for i in range(n):
        for j in range(m):
            print(i + j, end=" ")
        print()


if __name__ == "__main__":
    main()
