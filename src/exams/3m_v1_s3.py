def main() -> None:
    n = int(input("Quanti nomi di animali inserire? "))
    if n <= 0:
        print("Errore: n deve essere positivo.")
        return
    
    animali = []
    for _ in range(n):
        animale = input("Inserisci un nome di animale: ").strip().lower()
        if not animale:
            print("Errore: nome vuoto.")
            return
        animali.append(animale)
    
    vocali = []
    for animale in animali:
        if animale[0] in "aeiou":
            vocali.append(animale)
    
    num_vocali = len(vocali)
    num_consonanti = len(animali) - num_vocali
    
    print(f"Animali con vocale: {num_vocali}")
    print(vocali)
    print(f"Animali con consonante: {num_consonanti}")

if __name__ == "__main__":
    main()