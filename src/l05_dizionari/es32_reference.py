def main() -> None:
    citta = {"Roma": 2870000, "Milano": 1350000, "Napoli": 975000}

    for nome, pop in citta.items():
        print(f"{nome}: {pop} abitanti")


if __name__ == "__main__":
    main()
