def fattoriale(n: int) -> int:
    """Calcola il fattoriale di un numero usando la ricorsione."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fattoriale(n - 1)


# Programma principale
n = int(input("Inserisci un numero intero positivo: "))
if n < 0:
    print("Il fattoriale non è definito per numeri negativi.")
else:
    risultato = fattoriale(n)
    print(f"Il fattoriale di {n} è: {risultato}")
