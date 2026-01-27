def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    try:
        n = int(input("Inserisci n (>= 0): "))
        if n < 0:
            print("Errore: n deve essere un numero intero non negativo.")
        else:
            risultato = fibonacci(n)
            print(f"Il {n}-esimo numero di Fibonacci è: {risultato}")
    except ValueError:
        print("Errore: inserisci un numero intero valido.")