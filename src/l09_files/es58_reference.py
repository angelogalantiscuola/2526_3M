import json


def salva_studenti(studenti: list[dict], nome_file: str) -> None:
    """Salva una lista di studenti in un file JSON."""
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(studenti, file, indent=4)
        print(f"File '{nome_file}' salvato con successo.")
    except IOError as e:
        print(f"Errore durante il salvataggio del file: {e}")


def carica_studenti(nome_file: str) -> list[dict]:
    """Carica una lista di studenti da un file JSON."""
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            studenti = json.load(file)
        return studenti
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non è stato trovato.")
        return []
    except json.JSONDecodeError as e:
        print(f"Errore nel parsing JSON: {e}")
        return []


def calcola_media(studenti: list[dict]) -> float:
    """Calcola la media dei voti degli studenti."""
    if not studenti:
        return 0.0
    somma = sum(studente["voto"] for studente in studenti)
    return somma / len(studenti)


def main() -> None:
    """Funzione principale."""
    studenti = [
        {"nome": "Alice", "voto": 8},
        {"nome": "Bob", "voto": 7},
        {"nome": "Carlo", "voto": 9}
    ]
    
    nome_file = "studenti.json"
    salva_studenti(studenti, nome_file)
    
    studenti_caricati = carica_studenti(nome_file)
    if studenti_caricati:
        print(f"Studenti caricati: {studenti_caricati}")
        media = calcola_media(studenti_caricati)
        print(f"Media voti: {media:.1f}")


# Avvio del programma
if __name__ == "__main__":
    main()