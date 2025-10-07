def main() -> None:
    nome: str = input("Inserisci il tuo nome: ")
    eta: int = int(input("Inserisci la tua età: "))
    
    print(f"Ciao {nome}!")
    
    if eta < 18:
        print("Sei minorenne.")
    elif eta < 65:
        print("Sei adulto.")
    else:
        print("Sei anziano.")

if __name__ == "__main__":
    main()