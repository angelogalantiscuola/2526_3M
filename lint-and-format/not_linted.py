"""Esempio di file Python con vari problemi di stile e convenzioni.
Errori di linting comuni includono:
- Confronto con None usando `==` invece di `is`/`is not`.
- Variabili inutilizzate.
- Istruzioni composte sulla stessa riga e spaziatura incoerente.

Controlla questo file con uno strumento di linting per identificare e correggere i problemi.
Usa ruff examples/not_linted.py per eseguire il linting.
"""


def main():
    x = 1
    result = None
    if x == None:  # confronto errato con None
        result = 0
    unused_variable = "I am never used"  # variabile inutilizzata
    print("Result is:", result)

    n = 4
    for i in range(0, n):
        if i % 2 == 0: print(i, end=" ")  # istruzione composta su una riga

    return result


if __name__ == "__main__":
    main()
