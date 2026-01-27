def aggiungi_elemento(lista: list[dict]) -> bool:
    """Aggiunge un elemento alla lista chiedendo nome e prezzo."""
    nome = input("Nome elemento: ")
    if not nome:
        return False
    if nome.isdigit():
        return False
    try:
        prezzo = float(input("Prezzo: "))
    except ValueError:
        return False
    nuovo_elemento = {"nome": nome, "prezzo": prezzo}
    lista.append(nuovo_elemento)
    return True


def rimuovi_elemento(lista: list[dict]) -> None:
    """Rimuove un elemento dalla lista per nome."""
    nome = input("Nome da rimuovere: ")
    for item in lista:
        if item["nome"] == nome:
            lista.remove(item)
            print("Elemento rimosso.")
            return
    print("Elemento non trovato.")


def visualizza_lista(lista: list[dict]) -> None:
    """Visualizza tutti gli elementi della lista."""
    if not lista:
        print("Lista vuota.")
        return
    for item in lista:
        print(f"{item['nome']}: {item['prezzo']}€")


def calcola_totale(lista: list[dict]) -> float:
    """Calcola e restituisce il totale dei prezzi."""
    totale = 0.0
    for item in lista:
        totale += item["prezzo"]
    return totale


def main() -> None:
    """Funzione principale con menu interattivo."""
    lista: list[dict] = []
    while True:
        print("\nMenu:")
        print("1. Aggiungi elemento")
        print("2. Rimuovi elemento")
        print("3. Visualizza lista")
        print("4. Calcola totale")
        print("5. Esci")
        scelta = input("Scegli: ")
        if scelta == "1":
            if aggiungi_elemento(lista) is True:
                print("Elemento aggiunto.")
            else:
                print("Errore nell'aggiunta dell'elemento.")
        elif scelta == "2":
            rimuovi_elemento(lista)
        elif scelta == "3":
            visualizza_lista(lista)
        elif scelta == "4":
            totale = calcola_totale(lista)
            print(f"Totale: {totale}€")
        elif scelta == "5":
            break
        else:
            print("Scelta non valida.")


# Avvio del programma
main()
