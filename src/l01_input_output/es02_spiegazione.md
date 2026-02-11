# if __name__ == "__main__:" - Spiegazione Pratica

## Cos'è?

`if __name__ == "__main__":` è un costrutto Python che ti permette di distinguere tra:

- **Esecuzione diretta**: quando esegui lo script direttamente (`python es02_modulo.py`)
- **Importazione**: quando il file è importato in un altro script (`from es02_modulo import ...`)

## Perché serve?

Permette al tuo codice di avere comportamenti diversi a seconda di come viene usato:

```python
# ✅ Codice che vuoi usare da otros script
def calcola_eta(anno_nascita):
    return 2025 - anno_nascita

# ⚙️ Codice di test/demo che esegui SOLO quando lanci il file direttamente
if __name__ == "__main__":
    print(calcola_eta(1990))  # Solo se esecuzione diretta
```

## Come funziona?

**Quando Python avvia uno script:**
- `__name__` viene impostato a `"__main__"`
- Il blocco `if __name__ == "__main__":` **VIENE ESEGUITO**

**Quando Python importa un modulo:**
- `__name__` viene impostato al nome del modulo (es. `"es02_modulo"`)
- Il blocco `if __name__ == "__main__":` **NON VIENE ESEGUITO**

## Proprietà del valore di __name__

```python
# es02_modulo.py
print(__name__)  # Se eseguito: "__main__"
                 # Se importato: "es02_modulo"
```

## Esperimento pratico

### 1️⃣ Esegui il modulo direttamente
```bash
python es02_modulo.py
# Output:
# 📌 ATTENZIONE: es02_modulo.py è stato eseguito DIRETTAMENTE
# Questo è codice di test del modulo.
# Ciao Marco! Hai 35 anni.
```

### 2️⃣ Usa il modulo da uno script principale
```bash
python es02_main.py
# Output:
# 📌 ATTENZIONE: es02_main.py è stato eseguito DIRETTAMENTE
# === Questo script importa il modulo es02_modulo ===
# 
# Inserisci il tuo nome: Luigi
# Inserisci il tuo anno di nascita: 1995
# Ciao Luigi! Hai 30 anni.
```

**Nota**: Il messaggio del modulo ("ATTENZIONE: es02_modulo.py è stato eseguito...") **NON appare** perché il modulo viene importato, non eseguito direttamente!

## Vantaggi

✅ **Riutilizzabilità**: puoi scrivere funzioni che altri possono importare  
✅ **Test integrato**: puoi aggiungere test direttamente nel file senza infastidire chi lo importa  
✅ **Organizzazione**: separa il codice utile dal codice di prova  
✅ **Best practice**: è lo standard in Python per strutturare i progetti

## Regola d'oro

> **Il codice importante che vuoi riutilizzare va FUORI da `if __name__ == "__main__":`**  
> **Il codice di test/demo va DENTRO `if __name__ == "__main__":`**
