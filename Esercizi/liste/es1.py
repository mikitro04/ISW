# Scrivere una funzione che prenda come argomento una lista
#  di numeri.
# Tale funzione deve restituire la media e la deviazione
#  standard dei numeri presenti all’interno della lista.

def devStdEMedia(l):
    sommatoria = 0
    for el in l:
        sommatoria += el
    media = sommatoria / len(l)     # Primo risultato

    devStd = 0
    for el in l:
        x = el - media
        x = x ** 2
        devStd += x
    devStd = devStd / len(l)
    devStd = devStd ** 0.5

    return (media, devStd)

lista = [10, 12, 23, 23, 16, 23, 21, 16]

(m, d) = devStdEMedia(lista)
print(f'la media e\' {m} mentre la deviazione standard e\' {d}')