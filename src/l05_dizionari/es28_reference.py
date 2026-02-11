def main() -> None:
    studenti = {"Mario": [8, 9, 8], "Luca": [7, 7, 7], "Anna": [9, 10, 8]}

    for nome in studenti:
        voti = studenti[nome]
        media = sum(voti) / len(voti)
        print(f"{nome}: Media voti = {media:.1f}")


if __name__ == "__main__":
    main()
