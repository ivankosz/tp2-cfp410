def generador_contraseñas2(caracter, cant):
    import string
    import random
    from random import choice
    alfamin=string.ascii_lowercase
    alfamay=string.ascii_uppercase
    numeros=string.digits
    especiales=string.punctuation
    bolsa=alfamin+alfamay+numeros+especiales

    contraseñas=list()
    if caracter==4:
        for a in range(cant):
            cadena=choice(alfamin)+choice(alfamay)+choice(numeros)+choice(especiales)
            l=list(cadena)
            random.shuffle(l)
            result=''.join(l)
            contraseñas.append(result)
        return contraseñas

    else:
        for a in range(cant):
            cadena=choice(alfamin)+choice(alfamay)+choice(numeros)+choice(especiales)
            for b in range(caracter-4):
                resto=choice(bolsa)
                cadena+=resto
                l=list(cadena)
                random.shuffle(l)
                result=''.join(l)
            contraseñas.append(result)
        return contraseñas

if __name__ == "__main__":
    print(len(generador_contraseñas2(10, 10)))
    print(generador_contraseñas2(10, 10))
