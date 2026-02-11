"""
Script principale che IMPORTA e usa il modulo es02_modulo.

Quando il modulo viene importato, il codice all'interno di 
if __name__ == "__main__": NON viene eseguito.
"""

from es02_modulo import calcola_eta, saluta_utente


def main() -> None:
    print("📌 ATTENZIONE: es02_main.py è stato eseguito DIRETTAMENTE\n")
    print("=== Questo script importa il modulo es02_modulo ===\n")
    
    # Usiamo le funzioni del modulo
    nome_utente: str = input("Inserisci il tuo nome: ")
    anno_nascita_str: str = input("Inserisci il tuo anno di nascita: ")
    anno_nascita_int: int = int(anno_nascita_str)
    
    eta = calcola_eta(anno_nascita_int)
    saluta_utente(nome_utente, eta)


if __name__ == "__main__":
    main()
