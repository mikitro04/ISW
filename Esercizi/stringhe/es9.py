# Scrivere una funzione che chieda all’utente di inserire una
#  frase di almeno 20 lettere e che ripeta la richiesta fino a che
#  non sia soddisfatta.

while True:
    s = input('Inserisci una stringa di 20 caratteri o piu\': ')
    if len(s) >= 20:
        break
    else:
        print('Inserisci piu\' di 20 caratteri!')