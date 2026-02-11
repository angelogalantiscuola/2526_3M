# ## Esempio
# Per 3 numeri: 4, 7, 10  
# Somma = 21, Media = 7.00.

def main() -> None:
    print("Media di una lista di numeri")
    print("Il programma Python che chieda all'utente quanti numeri inserire, li legga uno per uno, li memorizzi in una lista e calcoli la media aritmetica.")
    # INPUT 1. Richiedere all'utente di inserire il numero di valori da considerare (numero intero positivo).
    numero_valori: int = int(input("Inserisci il numeri di valori di cui calcolare la media: "))

    # INPUT 2. Utilizzare un ciclo per leggere ciascun numero dall'utente e aggiungerlo a una lista vuota (inizializzata come `numeri = []`).
    la_mia_lista: list[int] = []
    for _ in range(numero_valori):
        numero_inserito: int = int(input("Inserisci un numero: "))
        la_mia_lista.append(numero_inserito)
    print(f"Controllo la lista {la_mia_lista}")
    
    # ELABORAZIONE 3. Dopo aver raccolto tutti i numeri, calcolare la somma degli elementi della lista e dividerla per il numero di elementi per ottenere la media.
    somma: int = 0
    for numero in la_mia_lista:
        somma = somma + numero
        # somma += numero
    print(f"La somma dei numeri inseriti vale: {somma}")
    if numero_valori != 0:
        media: float = somma / numero_valori
    else:
        media: float = 0.0
    
    # OUTPUT 4. Gestire il caso in cui la lista sia vuota (numero di valori = 0), stampando un messaggio di errore.
    if la_mia_lista == []:
        print("la lista e' vuota")

    # OUTPUT 5. Stampare la media calcolata con due decimali, ad esempio: "La media dei numeri inseriti è: [media]".
    print(f"La media vale: {media:.2f}")


if __name__ == "__main__":
    main()