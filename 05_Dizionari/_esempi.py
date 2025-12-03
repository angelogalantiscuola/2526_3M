# automobile: modello, marca, anno, chilometraggio, proprietario
# proprietario: nome, cognome, età, indirizzo
# indirizzo: via, numero, città, CAP
# tagliandi: anno, chilometraggio, officina

automobile: dict[str, any] = {
    "modello": "Model S",
    "marca": "Tesla",
    "anno": 2020,
    "chilometraggio": 15000,
    "proprietario": {
        "nome": "Alice",
        "cognome": "Rossi",
        "età": 30,
        "indirizzo": {
            "via": "Via Milano",
            "numero": 5,
            "città": "Roma",
            "CAP": 13100,
        },
    },
    "tagliandi": [
        {"anno": 2021, "chilometraggio": 5000, "officina": "Officina A"},
        {"anno": 2022, "chilometraggio": 10000, "officina": "Officina B"},
    ],
}

# # Un dizionario che descrive uno studente


studente: dict[str, any] = {
    "nome": "Bob",
    "eta": 12,
    "promosso": True,
    "voti": [8.5, 7.0, 9.0],
    "indirizzo": {
        "via": "Via Roma",
        "numero": 10,
        "citta": "Milano",
        "cap": 20100,
    },
    "contatti": {
        "email": "bob@example.com",
        "telefono": [
            {"tipo": "casa", "numero": "123-456-7890"},
            {"tipo": "cellulare", "numero": "098-765-4321"},
        ],
    },
}

lista = [1, 5, 8, 12, 20, 25]
print(len(lista))  # 6

print(len(studente))  # 6 (nome, eta, promosso, voti, indirizzo, contatti)
print(len(studente["voti"]))  # 3 (8.5, 7.0, 9.0)
print(len(studente["indirizzo"]))  # 4 (via, numero, citta, cap)

# salvare i voti della stessa materia meglio una lista
voti = [
    8.523232,
    7.0,
    9.0,
]

# se voglio associare i voti alle materie meglio un dizionario
voti_di_tutte_le_materie = {
    "matematica": [8.5, 9, 7.5],
    "italiano": [7.0, 6.5, 8.0],
    "scienze": [9.0, 8.5, 9.5],
}

pagella = {
    "nome": "Bob",
    "eta": 12,
    "promosso": True,
    "matematica": 7,
    "italiano": 6,
    "scienze": 9,
}
print(len(pagella))
print(type(pagella["nome"]))  # str
print(type(pagella["eta"]))  # int
print(type(pagella["promosso"]))  # bool
print(type(pagella))  # dict

print(pagella["matematica"])  # 7
print(pagella.get("matematica"))  # 7
# oppure


pagella = {
    "matematica": 7,
    "italiano": 6,
    "scienze": 9,
}

print(pagella.keys())  # dict_keys(['matematica', 'italiano', 'scienze'])
print(pagella.values())  # dict_values([7, 6, 9])
print(
    pagella.items()
)  # dict_items([('matematica', 7), ('italiano', 6), ('scienze', 9)])

# keys(), values(), items()
for materia in pagella.keys():
    print(materia)
for voto in pagella.values():
    print(voto)
for materia, voto in pagella.items():
    print(f"{materia}: {voto}")

# media dei voti
somma = 0
for voto in pagella.values():  # 7, 6, 9
    somma = somma + voto
    # somma = 0 + 7 = 7
    # somma = 7 + 6 = 13
    # somma = 13 + 9 = 22
media = somma / len(pagella)
print(f"Media voti: {media}")  # Media voti: 7.333333333333333


pagella = {
    "matematica": 7,
    "italiano": 6,
    "scienze": 9,
}

print(pagella.keys())  # dict_keys(['matematica', 'italiano', 'scienze'])
print(pagella.values())  # dict_values([7, 6, 9])
print(
    pagella.items()
)  # dict_items([('matematica', 7), ('italiano', 6), ('scienze', 9)])

for voto in pagella.values():  # [7, 6, 9]
    print(voto)
# for voto in [7, 6, 9]:
#     print(voto)

# stampare elenco materie
for materia in pagella.keys():
    print(materia)

# stampare elenco materie con voti
for materia, voto in pagella.items():
    print(f"{materia}: {voto}")


pagella = {
    "matematica": 7,
    "italiano": 6,
    "scienze": 9,
}

print("Prima dell'aggiornamento:")
print(pagella)

pagella.pop("italiano")  # rimuove la materia italiano
print("Dopo la rimozione di italiano:")
print(pagella)
