def main() -> None:
    anno: int = int(input("Inserisci un anno: "))
    
    if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
        print(f"L'anno {anno} è bisestile.")
    else:
        print(f"L'anno {anno} non è bisestile.")

if __name__ == "__main__":
    main()