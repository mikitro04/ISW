def verStr (s):
    cifreValide = '1234567890'
    for char in s:
        if char not in cifreValide:
            return False
    return True

print(verStr(input("Inserisci stringa: ")))