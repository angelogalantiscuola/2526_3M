def chiedi_numeri() -> list[float]:
    """Chiede all'utente due numeri e li restituisce in una lista."""
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))
    return [num1, num2]


def scegli_operazione() -> str:
    """Mostra un menu e restituisce l'operazione scelta."""
    print("Scegli un'operazione:")
    print("1. Addizione (+)")
    print("2. Sottrazione (-)")
    print("3. Moltiplicazione (*)")
    print("4. Divisione (/)")
    scelta = input("Inserisci il numero dell'operazione: ")
    if scelta == "1":
        return "+"
    elif scelta == "2":
        return "-"
    elif scelta == "3":
        return "*"
    elif scelta == "4":
        return "/"
    else:
        return ""


def calcola(num1: float, num2: float, operazione: str) -> float | None:
    """Esegue il calcolo e restituisce il risultato."""
    if operazione == "+":
        return num1 + num2
    elif operazione == "-":
        return num1 - num2
    elif operazione == "*":
        return num1 * num2
    elif operazione == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Errore: divisione per zero!")
            return None
    else:
        return None


def main() -> None:
    """Funzione principale che orchestra il programma."""
    print("Benvenuto nella Calcolatrice Modulare!")
    numeri = chiedi_numeri()
    operazione = scegli_operazione()
    risultato = calcola(numeri[0], numeri[1], operazione)

    if risultato is not None:
        print(f"Il risultato è: {risultato}")
    else:
        print("Operazione non valida.")


# Avvio del programma
main()
