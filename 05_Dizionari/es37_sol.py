def main() -> None:
    persone = [
        {"nome": "Mario", "età": 30, "città": "Milano"},
        {"nome": "Luca", "età": 25, "città": "Roma"},
        {"nome": "Anna", "età": 35, "città": "Milano"},
        {"nome": "Giovanni", "età": 28, "città": "Napoli"},
        {"nome": "Sofia", "età": 22, "città": "Milano"},
    ]

    # Trova età massima
    eta_massima = 0
    for persona in persone:
        if persona["età"] > eta_massima:
            eta_massima = persona["età"]

    # Trova la persona con età massima (primo match)
    persona_massima = None
    for persona in persone:
        if persona["età"] == eta_massima:
            persona_massima = persona
            break

    # Stampa dettagli
    for persona in persone:
        print(
            f"Nome: {persona['nome']}, Età: {persona['età']}, Città: {persona['città']}"
        )

    print(f"Età massima: {eta_massima}")
    if persona_massima:
        print(
            f"Persona con età massima: Nome: {persona_massima['nome']}, Età: {persona_massima['età']}, Città: {persona_massima['città']}"
        )


if __name__ == "__main__":
    main()
