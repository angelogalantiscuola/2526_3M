# 2526_3M

## Sintesi concisa degli errori

- `examples/not_formatted.py`
	- Indentazione incoerente: la seconda stampa è indentata di un livello non corretto.
	- Linee vuote multiple alla fine del file.

- `examples/not_linted.py`
	- Confronto con None usando `==` (usa `is None`).
	- Variabile assegnata e non usata (`unused_variable`).
	- Istruzione composta sulla stessa riga (`if i % 2 == 0: print(...)`) – separare su più righe.

Comandi rapidi per verificare gli errori:

```bash
# controlla errori di formattazione
ruff format --check examples/not_formatted.py

# controlla errori di linting
ruff check examples/not_linted.py
``` 

### c) Integrazione con VSCode

La vera potenza di Ruff si ottiene integrandolo in VSCode.

1.  Installa l'estensione **"Ruff"** dal marketplace di VSCode (autori: charliermarsh o simili).
2.  Configura VSCode per formattare il codice automaticamente al salvataggio. Apri le impostazioni utente/di workspace (file `settings.json`) e aggiungi o aggiorna questa sezione:

```json
"[python]": {
	"editor.defaultFormatter": "charliermarsh.ruff",
	"editor.formatOnSave": true,
	"editor.codeActionsOnSave": {
		"source.fixAll": "explicit"
	}
}
```

Con questa configurazione, ogni volta che salvi un file Python, Ruff proverà a risolvere automaticamente errori di linting e applicherà la formattazione (se abilitata dall'estensione). È un modo rapido per mantenere il codice pulito e coerente.

### Nota su `settings.json`

Quando modifichi `settings.json`, fai attenzione a non rimuovere le parentesi graffe esterne `{ ... }` del file: se il file contiene già altre impostazioni, aggiungi solo la sezione "[python]" al suo interno. Esempio conciso:

```json
// settings.json preesistente
{
	"editor.fontSize": 14
}

// dopo l'aggiunta, mantieni le parentesi esterne e unisci le sezioni
{
	"editor.fontSize": 14,
	"[python]": {
		"editor.defaultFormatter": "charliermarsh.ruff",
		"editor.formatOnSave": true,
		"editor.codeActionsOnSave": { "source.fixAll": "explicit" }
	}
}
```

Se il file è vuoto, inserisci l'intera struttura con le parentesi esterne come mostrato.

