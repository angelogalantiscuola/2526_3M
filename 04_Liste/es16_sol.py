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
    minimo = numeri[0]
    for num in numeri:
        if num > massimo:
            massimo = num
        if num < minimo:
            minimo = num

    range_val = massimo - minimo
    print(f"Il range dei numeri inseriti è: {range_val}")


if __name__ == "__main__":
    main()
