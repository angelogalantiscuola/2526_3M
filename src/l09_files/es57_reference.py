def conta_parole(nome_file: str) -> dict[str, int]:
    """Legge un file e conta le occorrenze di ogni parola (case-insensitive, senza punteggiatura)."""
    conteggio = {}
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            contenuto = file.read().lower()
            # Rimuovi punteggiatura semplice
            contenuto = contenuto.replace(".", "").replace(",", "")
            parole = contenuto.split()
            for parola in parole:
                if parola in conteggio:
                    conteggio[parola] += 1
                else:
                    conteggio[parola] = 1
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non è stato trovato.")
    except IOError as e:
        print(f"Errore durante la lettura del file: {e}")
    return conteggio


def stampa_conteggio(dizionario: dict[str, int]) -> None:
    """Stampa il dizionario in ordine alfabetico."""
    print("Conteggio parole:")
    for parola, numero in sorted(dizionario.items()):
        print(f"{parola}: {numero}")


def main() -> None:
    """Funzione principale."""
    testo = "Python è un linguaggio di programmazione. Python è semplice e potente."
    
    nome_file = "esercizio57.txt"
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            file.write(testo)
        print(f"File '{nome_file}' creato con successo.")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")
        return
    
    dizionario_conteggio = conta_parole(nome_file)
    stampa_conteggio(dizionario_conteggio)


# Avvio del programma
if __name__ == "__main__":
    main()