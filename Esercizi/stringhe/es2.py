def isPunt (s):
    punteggiatura = '.,><;:"\'\\|[]`~-_)(*&^%$#@!/?}{'
    for c in s:
        if c in punteggiatura:
            return True
    return False

print(isPunt(input('Inserisci stringa: '))) # True se ha punteggiatura, altimenti False