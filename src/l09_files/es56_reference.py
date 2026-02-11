def scrivi_file(frasi: list[str], nome_file: str) -> None:
    """Scrive una lista di frasi su un file, una per riga."""
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            for frase in frasi:
                file.write(frase + "\n")
        print(f"File '{nome_file}' scritto con successo.")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")


def leggi_file(nome_file: str) -> list[str]:
    """Legge un file e restituisce una lista di righe senza newline."""
    righe = []
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            for riga in file:
                righe.append(riga.strip())
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non è stato trovato.")
    except IOError as e:
        print(f"Errore durante la lettura del file: {e}")
    return righe


def main() -> None:
    """Funzione principale."""
    frasi = ["Ciao mondo", "Python è divertente", "File handling"]
    
    nome_file = "esercizio56.txt"
    scrivi_file(frasi, nome_file)
    
    righe_lette = leggi_file(nome_file)
    print("Contenuto del file:")
    for riga in righe_lette:
        print(riga)


# Avvio del programma
if __name__ == "__main__":
    main()