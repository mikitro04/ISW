# Scrivere una funzione che chieda all’utente di inserire una
#  parola e che sia in grado di capire se la parola inserita è un
#  palindromo o no.

# Torna True o False.

# Esempi: radar, ingegni, osso.

def isPalindome (s):
    if s == s[::-1]:        # [::-1] = sarebbe da inizio a fine(:) con passo -1, quindi al contrario (:-1)
        return True
    else:
        return False

print(isPalindome(input('Inserisci stringa: ')))