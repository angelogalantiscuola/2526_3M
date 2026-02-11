# Stringa piu' lunga (es17)
# Chiedere all'utente N stringhe e trovare quella piu' lunga

n: int = int(input("inserisci il numero di stringhe che vuoi inserire: "))

if n < 0:
    print("valore errato")

max_len = 0
longest = ""
for i in range(n):
    s: str = input(f"inserisci la stringa #{i+1}: ")
    l = len(s)
    if l > max_len:
        max_len = l
        longest = s

print(f"La stringa più lunga è: '{longest}' con {max_len} caratteri")
