# Scrivere una funzione che accetti in ingresso una stringa e che
#  stampi il numero di lettere minuscole e maiuscole presenti nella
#  stringa.

# Si accettano anche stringhe contenenti sia lettere che
#  numeri/caratteri (esempio “ciao45”), mentre non si accettano
#  stringhe contenenti solo caratteri (esempio “!##+”), in tal caso la
#  funzione deve stampare il messaggio: “La stringa di input non
#  contiene lettere”.

def printNumberOfCase(s):
    upper = 0
    lower = 0
    upperS = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    lowerS = 'qwertyuiopasdfghjklzxcvbnm'
    numberS = '1234567890'

    for c in s:
        if c in upperS:
            upper += 1
        elif c in lowerS:
            lower += 1
        elif c in numberS:
            continue
        else:
            raise ValueError('Non puoi inserire caratteri speciali!')
    print ('In upperCase: {} \nIn lowerCase: {}'.format(upper, lower) )

printNumberOfCase(input('input: '))