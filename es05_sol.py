import math

def main() -> None:
    a: float = float(input("Inserisci il coefficiente a: "))
    b: float = float(input("Inserisci il coefficiente b: "))
    c: float = float(input("Inserisci il coefficiente c: "))
    
    discriminante: float = b**2 - 4*a*c
    
    if discriminante > 0:
        x1: float = (-b + math.sqrt(discriminante)) / (2*a)
        x2: float = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Le soluzioni sono x1 = {x1} e x2 = {x2}")
    elif discriminante == 0:
        x: float = -b / (2*a)
        print(f"La soluzione doppia è x = {x}")
    else:
        print("Non ci sono soluzioni reali.")

if __name__ == "__main__":
    main()