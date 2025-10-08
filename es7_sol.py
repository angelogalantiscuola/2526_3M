def main() -> None:
    lato1: float = float(input("Inserisci la lunghezza del primo lato: "))
    lato2: float = float(input("Inserisci la lunghezza del secondo lato: "))
    lato3: float = float(input("Inserisci la lunghezza del terzo lato: "))
    
    # Trova il lato più lungo
    ipotenusa: float = max(lato1, lato2, lato3)
    
    # Calcola la somma dei quadrati degli altri due
    if ipotenusa == lato1:
        somma_quadrati: float = lato2**2 + lato3**2
    elif ipotenusa == lato2:
        somma_quadrati: float = lato1**2 + lato3**2
    else:
        somma_quadrati: float = lato1**2 + lato2**2
    
    # Verifica se è rettangolo
    if abs(ipotenusa**2 - somma_quadrati) < 1e-6:  # Tolleranza per floating point
        print("Il triangolo è rettangolo.")
    else:
        print("Il triangolo non è rettangolo.")

if __name__ == "__main__":
    main()