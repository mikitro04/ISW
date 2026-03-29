# a) Scrivere il codice di una funzione che, data una stringa e un
#  carattere, verifica se il carattere compare doppio
#  (consecutivamente) nella stringa.

# def isDouble(s, c):
#     flag = False
#     for char in s:
#         if c == char and not flag:  # primo carattere uguale
#             flag = True
#         elif c == char and flag:    # secondo carattere uguale
#             return True
#         else:
#             flag = False
#     return False
        
# print(isDouble(input('Inserisci stringa: '), input('Inserisci carattere da verificare doppio consecutivo: ')))


# b) Scrivere una seconda funzione che data una stringa verifica se
#  al suo interno ci siano doppie (2 caratteri uguali consecutivi), se
#  sì li stampa.

def thereIsDuble(s):
    firstTime = True
    res = ''
    ress = False
    for char in s:
        if firstTime:
            c = char
            firstTime = False
            continue
        else:
            if char == c:
                res = res + c + c
                ress = True
            else:
                c = char
    if ress:
        return res
    else:
        return False
        
print(thereIsDuble(input('Inserisci stringa: ')))