# Scrivere il codice di una funzione che accetti una stringa e un
#  carattere e restituisca la posizione del carattere all’interno della
#  stringa, -1 se non c’è.

def whereIs(s, c):
    i = 1
    for char in s:
        if char == c:
            return i
        else:
            i += 1
    return -1

print(whereIs(input('Inserisci stringa: '), input('Inserisci carattere da ricercare: ')))