def main() -> None:
    n = int(input("Inserisci il numero di valori da considerare: "))
    if n <= 0:
        print("Errore: numero di valori deve essere positivo.")
        return

    numeri = []
    for _ in range(n):
        numero = int(input("Inserisci un numero: "))
        numeri.append(numero)

    if not numeri:
        print("Errore: lista vuota.")
        return

    conteggio_pari = 0
    for num in numeri:
        if num % 2 == 0:
            conteggio_pari += 1

    print(f"Il numero di numeri pari inseriti è: {conteggio_pari}")


if __name__ == "__main__":
    main()
