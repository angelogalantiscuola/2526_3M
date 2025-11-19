# INPUT
n: int = int(input("Inserisci il valore n: "))
c: str = input("Inserisci una lettera c: ")
x: int = int(input("Inserisci il valore x: "))

# CHECK
if n <= 0:
    print("Errore: n deve essere un intero positivo.")
    exit(1)
if len(c) != 1 or not c.isalpha():
    print("Errore: c deve essere una singola lettera.")
    exit(1)
if x <= 0:
    print("Errore: x deve essere un intero positivo.")
    exit(1)

# ELABORAZIONE
lista_stringhe_filtrate: list[str] = []
stringhe_inserite: list[str] = []
for _ in range(n):
    stringa_utente = input("Inserisci una stringa: ")
    stringhe_inserite.append(stringa_utente)
    if c in stringa_utente and len(stringa_utente) > x:
        lista_stringhe_filtrate.append(stringa_utente)


print(f"Stringhe con '{c}' e più lunghe di {x}: {lista_stringhe_filtrate}")
print(f"Numero di stringhe che contengono '{c}' e sono più lunghe di {x}: {len(lista_stringhe_filtrate)}")

# Calcola la lunghezza minima
lunghezza_minima: int = min(len(s) for s in lista_stringhe_filtrate)

# OUTPUT
print(f"Lunghezza minima delle stringhe che contengono '{c}' e sono più lunghe di {x}: {lunghezza_minima}")