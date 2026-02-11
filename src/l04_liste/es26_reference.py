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

    # Bubble sort semplificato (inefficiente)
    for i in range(len(numeri)):
        for j in range(len(numeri) - 1):
            if numeri[j] > numeri[j + 1]:
                temp = numeri[j]
                numeri[j] = numeri[j + 1]
                numeri[j + 1] = temp

    print(f"Lista originale: {numeri}")
    print(f"Lista ordinata: {numeri}")


if __name__ == "__main__":
    main()
