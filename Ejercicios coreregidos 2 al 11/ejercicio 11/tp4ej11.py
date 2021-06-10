################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 11: Palíndromo

def palindromo(palabra):
    palabra=str(palabra).lower().replace(" ","")
    return palabra==palabra[::-1]

def prueba():
    frase=input("Ingrese una frase o palabra para verificar si es palindromo: ")
    res = palindromo(frase)
    print (res)

if __name__ == "__main__":
    prueba()