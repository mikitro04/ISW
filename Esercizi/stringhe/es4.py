# Scrivere una funzione che accetta una stringa e che, se esiste
#  un punto '.' nella stringa, ne restituisce l’ultima parte, cioe'
#  quella che segue il punto.
# 
# Esempio: "ciao .a tutti. ecco" -> "ecco "

def dopoIlPunto(s):
    res = ''
    flag = False
    for c in s:
        if flag:
            res = res + c
        if c == '.' and flag:
            res = ''
        elif c == '.':
            flag = True
    return res

print(dopoIlPunto(input('Inserisci stringa: ')))