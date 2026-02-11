def main() -> None:
    libri = {
        "1984": "Orwell",
        "Il Signore degli Anelli": "Tolkien",
        "Harry Potter": "Rowling",
    }

    print("Titoli dei libri:")
    for titolo in libri.keys():
        print(titolo)


if __name__ == "__main__":
    main()
