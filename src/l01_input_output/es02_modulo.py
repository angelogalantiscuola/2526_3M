"""
Modulo di utilità per il calcolo dell'età.
Questo file può essere:
1. Importato in altri script
2. Eseguito direttamente
"""

ANNO_CORRENTE: int = 2025


def calcola_eta(anno_nascita: int) -> int:
    """Calcola l'età di una persona."""
    return ANNO_CORRENTE - anno_nascita


def saluta_utente(nome: str, eta: int) -> None:
    """Stampa un saluto personalizzato."""
    print(f"Ciao {nome}! Hai {eta} anni.")


# Questo codice viene eseguito SOLO se il file è lanciato direttamente
# NON viene eseguito se il file è importato in un altro script
if __name__ == "__main__":
    print("📌 ATTENZIONE: es02_modulo.py è stato eseguito DIRETTAMENTE")
    print("Questo è codice di test del modulo.\n")
    
    # Test del modulo
    eta = calcola_eta(1990)
    saluta_utente("Marco", eta)
