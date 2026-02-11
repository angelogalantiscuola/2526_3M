def main() -> None:
    nome = input("Inserisci il tuo nome: ").strip()
    if not nome:
        print("Errore: nome vuoto.")
        return
    
    eta = int(input("Inserisci la tua età: "))
    if eta < 0:
        print("Errore: età negativa.")
        return
    
    hobby = input("Inserisci il tuo hobby: ").strip().lower()
    if not hobby:
        print("Errore: hobby vuoto.")
        return
    
    if eta < 18 and hobby == "sport":
        print("Gioca all'aperto!")
    elif eta >= 18 and hobby == "lettura":
        print("Leggi un libro avvincente!")
    else:
        print("Trova un nuovo hobby!")

if __name__ == "__main__":
    main()