def calcola_area_triangolo(base: float, altezza: float) -> float:
    """Calcola l'area di un triangolo."""
    return (base * altezza) / 2


# Programma principale
base = float(input("Inserisci la base del triangolo: "))
altezza = float(input("Inserisci l'altezza del triangolo: "))
area = calcola_area_triangolo(base, altezza)
print(f"L'area del triangolo è: {area}")
