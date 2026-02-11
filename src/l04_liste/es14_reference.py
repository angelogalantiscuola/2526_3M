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

    massimo = numeri[0]
    for num in numeri:
        if num > massimo:
            massimo = num

    print(f"Il massimo dei numeri inseriti è: {massimo}")


if __name__ == "__main__":
    main()
