# y=2/3*x-2
def funzione_matematica(x: float) -> float:
    return 2 / 3 * x - 2


# z=x+y addizione di x e y numeri interi
def somma(x: int, y: int) -> int:
    return x + y


# funzione che conta i caratteri di una stringa
def conta_caratteri(s: str) -> int:
    return len(s)


def sei_maggiore_di_18(eta: int) -> bool:
    return eta > 18


maggiorenne = sei_maggiore_di_18(4)  # false
if maggiorenne is True:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")


def saluta() -> None:
    print("Ciao, benvenuto nel programma!")


def saluta_personalizzato(nome: str) -> None:
    print(f"Ciao {nome}, benvenuto nel programma!")


def lancia_dado() -> int:
    import random

    return random.randint(1, 6)


def area_quadrato(lato: float) -> float:
    return lato * lato


# creare una funzione con piu parametri di ingresso e piu di un valore di ritorno
def calcola_rettangolo(base: float, altezza: float) -> tuple[float, float]:
    area = base * altezza
    perimetro = 2 * (base + altezza)
    return area, perimetro
