def main() -> None:
    hobby = {}
    for i in range(3):
        nome = input("Inserisci il nome della persona: ")
        hob = input("Inserisci l'hobby: ")
        hobby[nome] = hob

    print("Dizionario degli hobby:")
    for nome, hob in hobby.items():
        print(f"{nome}: {hob}")


if __name__ == "__main__":
    main()
