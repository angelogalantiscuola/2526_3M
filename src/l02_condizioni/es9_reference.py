def main() -> None:
    eccesso: int = int(input("Inserisci l'eccesso di velocità in km/h: "))
    
    if eccesso <= 10:
        multa = 36
    elif eccesso <= 40:
        multa = 148
    elif eccesso <= 60:
        multa = 370
    else:
        multa = 500
    
    print(f"La sanzione amministrativa è di euro {multa}.")

if __name__ == "__main__":
    main()