def main() -> None:
    N = int(input("Inserisci N: "))
    K = int(input("Inserisci K: "))
    A = int(input("Inserisci A: "))
    B = int(input("Inserisci B: "))

    if N <= 0 or K <= 0 or A >= B:
        print("Errore: input non validi.")
        return

    numeri_filtrati = []
    for _ in range(N):
        numero = int(input("Inserisci un numero: "))
        if numero % K == 0 and A <= numero <= B:
            numeri_filtrati.append(numero)

    print(f"Lista filtrata: {numeri_filtrati}")
    print(f"Numero di numeri: {len(numeri_filtrati)}")
    if numeri_filtrati:
        media = sum(numeri_filtrati) / len(numeri_filtrati)
        print(f"Media: {media}")


if __name__ == "__main__":
    main()
