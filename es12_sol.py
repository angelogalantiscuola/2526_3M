def main() -> None:
    estremo_inferiore: int = int(input("Inserisci l'estremo inferiore dell'intervallo: "))
    estremo_superiore: int = int(input("Inserisci l'estremo superiore dell'intervallo: "))
    
    somma: int = 0
    for numero in range(estremo_inferiore, estremo_superiore + 1):
        somma += numero
    
    print(f"La somma dei numeri nell'intervallo [{estremo_inferiore}, {estremo_superiore}] è: {somma}")

if __name__ == "__main__":
    main()