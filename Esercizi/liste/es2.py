# Scrivere una funzione che chieda all’utente di inserire una
#  serie di elementi (numeri, stringhe). Questi elementi
#  dovranno essere inseriti in una lista. La funzione deve
#  restituire una nuova lista contenente le coppie (index,item)
#  della lista precedente. 

def creaStringa():
    lista = []
    while True:
        dato = input("Inserisci un int e una stringa (end per concludere): ")

        if dato == "end":
            break

        listaDer = dato.split()
        if (listaDer[0]).isdigit():
            intero = int(listaDer[0])
        else:
            raise ValueError("devi inserire un intero")
        stringa = listaDer[1]
        lista.append((intero,stringa))
    
    return lista

print(creaStringa())