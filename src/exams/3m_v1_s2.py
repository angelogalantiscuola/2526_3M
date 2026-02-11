def main() -> None:
    n = int(input("Quanti numeri inserire? "))
    if n <= 0:
        print("Errore: n deve essere positivo.")
        return
    
    somma_pari = 0
    prodotto_dispari = 1
    totale = 0
    
    for _ in range(n):
        numero = int(input("Inserisci un numero: "))
        totale += numero
        if numero % 2 == 0 and numero > 0:
            somma_pari += numero
        elif numero % 2 != 0:
            prodotto_dispari *= numero
    
    media = totale / n
    print(f"Somma pari positivi: {somma_pari}")
    print(f"Prodotto dispari: {prodotto_dispari}")
    print(f"Media: {media:.2f}")

if __name__ == "__main__":
    main()