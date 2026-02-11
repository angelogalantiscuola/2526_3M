def main() -> None:
    nome = input("Inserisci il tuo nome: ")
    età = int(input("Inserisci la tua età: "))
    città = input("Inserisci la tua città: ")

    dizionario = {}
    dizionario["nome"] = nome
    dizionario["età"] = età
    dizionario["città"] = città

    print(f"Nome: {dizionario['nome']}")
    print(f"Età: {dizionario['età']}")
    print(f"Città: {dizionario['città']}")


if __name__ == "__main__":
    main()
