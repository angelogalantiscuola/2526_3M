def main() -> None:
    mese: str = input("Inserisci la sigla del mese (es. GEN): ").upper()
    
    if mese in ["DIC", "GEN", "FEB"]:
        stagione = "inverno"
    elif mese in ["MAR", "APR", "MAG"]:
        stagione = "primavera"
    elif mese in ["GIU", "LUG", "AGO"]:
        stagione = "estate"
    elif mese in ["SET", "OTT", "NOV"]:
        stagione = "autunno"
    else:
        print("Sigla mese inesistente.")
        return
    
    print(f"Il mese {mese} appartiene alla stagione: {stagione}.")

if __name__ == "__main__":
    main()