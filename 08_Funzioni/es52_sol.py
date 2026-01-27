def chiedi_peso() -> float:
    """Chiede il peso in kg e lo valida."""
    while True:
        try:
            peso = float(input("Inserisci il peso (kg): "))
            if peso > 0:
                return peso
            else:
                print("Il peso deve essere positivo.")
        except ValueError:
            print("Inserisci un numero valido.")


def chiedi_altezza() -> float:
    """Chiede l'altezza in metri e la valida."""
    while True:
        try:
            altezza = float(input("Inserisci l'altezza (m): "))
            if altezza > 0:
                return altezza
            else:
                print("L'altezza deve essere positiva.")
        except ValueError:
            print("Inserisci un numero valido.")


def calcola_bmi(peso: float, altezza: float) -> float:
    """Calcola e restituisce il BMI."""
    return peso / (altezza * altezza)


def classifica_bmi(bmi: float) -> str:
    """Classifica il BMI in una categoria."""
    if bmi < 18.5:
        return "Sottopeso"
    elif bmi < 25.0:
        return "Peso normale"
    elif bmi < 30.0:
        return "Sovrappeso"
    else:
        return "Obeso"


def get_colore_categoria(bmi: float) -> str:
    """Restituisce la categoria BMI con emoji."""
    if bmi < 18.5:
        return "🔵 Sottopeso"
    elif bmi < 25.0:
        return "🟢 Peso normale"
    elif bmi < 30.0:
        return "🟡 Sovrappeso"
    else:
        return "🔴 Obeso"


def stampa_risultato(peso: float, altezza: float, bmi: float, categoria: str) -> None:
    """Stampa il risultato del calcolo BMI in modo formattato."""
    print("\n=== Risultato BMI ===")
    print(f"Peso: {peso:.1f} kg")
    print(f"Altezza: {altezza:.2f} m")
    print(f"BMI: {bmi:.1f}")
    print(categoria)
    print()


def stampa_menu() -> None:
    """Stampa il menu principale."""
    print("\n=== Calcolatore BMI ===")
    print("1. Calcola BMI")
    print("2. Esci")


def main() -> None:
    """Funzione principale che orchestra il programma."""
    while True:
        stampa_menu()
        scelta = input("Scegli: ")

        if scelta == "1":
            peso = chiedi_peso()
            altezza = chiedi_altezza()
            bmi = calcola_bmi(peso, altezza)
            categoria = get_colore_categoria(bmi)
            stampa_risultato(peso, altezza, bmi, categoria)
        elif scelta == "2":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida.")


# Avvio del programma
main()

