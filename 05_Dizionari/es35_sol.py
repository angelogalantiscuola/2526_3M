def main() -> None:
    parole = ["rosso", "blu", "rosso", "verde", "blu"]

    frequenze = {}
    for parola in parole:
        if parola in frequenze:
            frequenze[parola] += 1
        else:
            frequenze[parola] = 1

    for parola, conteggio in frequenze.items():
        print(f"{parola}: {conteggio}")


if __name__ == "__main__":
    main()
