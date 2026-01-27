import random


def genera_numero() -> int:
    """Genera e restituisce un numero casuale tra 1 e 100."""
    return random.randint(1, 100)


def chiedi_tentativo() -> int:
    """Chiede all'utente di inserire un tentativo e lo restituisce come intero."""
    while True:
        try:
            tentativo = int(input("Indovina il numero (tra 1 e 100): "))
            return tentativo
        except ValueError:
            print("Errore: inserisci un numero intero valido.")


def verifica_tentativo(tentativo: int, numero_da_indovinare: int) -> str:
    """Verifica il tentativo e restituisce 'corretto', 'alto' o 'basso'."""
    if tentativo == numero_da_indovinare:
        return "corretto"
    elif tentativo > numero_da_indovinare:
        return "alto"
    else:
        return "basso"


def aggiorna_contatore(tentativi: int) -> int:
    """Incrementa e restituisce il numero di tentativi."""
    return tentativi + 1


def stampa_fine(tentativi: int, numero: int) -> None:
    """Stampa il messaggio di fine gioco."""
    print(f"Hai indovinato in {tentativi} tentativi! Il numero era {numero}.")


def main() -> None:
    """Funzione principale che orchestra il gioco."""
    print("Benvenuto nel gioco 'Indovina il numero'!")
    numero_da_indovinare = genera_numero()
    tentativi = 0


    while True:
        tentativo = chiedi_tentativo()
        feedback = verifica_tentativo(tentativo, numero_da_indovinare)
        if feedback == "corretto":
            break
        else:
            print(f"troppo {feedback}")
        tentativi = aggiorna_contatore(tentativi)

        print("Dentro il ciclo")

    # questa riga viene eseguita dopo il ciclo quando l'utente indovina
    stampa_fine(tentativi, numero_da_indovinare)


# Avvio del programma
main()
