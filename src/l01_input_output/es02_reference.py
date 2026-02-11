ANNO_CORRENTE: int = 2025

def main() -> None:
    nome_utente: str = input("Inserisci il tuo nome: ")
    anno_nascita_str: str = input("Inserisci il tuo anno di nascita: ")
    anno_nascita_int: int = int(anno_nascita_str)
    eta_utente: int = ANNO_CORRENTE - anno_nascita_int
    print(f"Ciao {nome_utente}! Quest'anno compi circa {eta_utente} anni.")

if __name__ == "__main__":
    main()