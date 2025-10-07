def main() -> None:
    a: float = float(input("Inserisci il coefficiente a: "))
    b: float = float(input("Inserisci il coefficiente b: "))
    
    if a == 0:
        if b == 0:
            print("L'equazione è indeterminata (infinite soluzioni).")
        else:
            print("L'equazione è impossibile (nessuna soluzione).")
    else:
        x: float = -b / a
        print(f"La soluzione è x = {x}")

if __name__ == "__main__":
    main()