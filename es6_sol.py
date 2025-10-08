def main() -> None:
    voto: float = float(input("Inserisci un voto numerico (tra 0 e 10, o negativo per uscire): "))
    
    if voto < 0:
        print("Uscita dal programma.")
    elif voto < 5:
        print("Giudizio: insufficiente")
    elif voto <= 6.5:
        print("Giudizio: sufficiente")
    elif voto <= 7.5:
        print("Giudizio: buono")
    elif voto <= 10:
        print("Giudizio: ottimo")
    else:
        print("Errore: voto fuori range.")

if __name__ == "__main__":
    main()