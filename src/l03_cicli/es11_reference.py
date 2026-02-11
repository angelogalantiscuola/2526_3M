def main() -> None:
    n: int = int(input("Inserisci il numero di valori da sommare: "))
    
    somma: int = 0
    for i in range(n):
        num: int = int(input(f"Inserisci il numero {i+1}: "))
        somma += num
    
    print(f"La somma totale è: {somma}")

if __name__ == "__main__":
    main()