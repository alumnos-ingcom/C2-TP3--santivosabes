################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 9: Numeros primos

def prueba():
    pass

def primo(numero):
    for x in range(2,numero):
        if numero% x == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True
while True:
    numero_ingresado=int(input("Ingrese un numero para verificar si es primo o no: "))
    primo(numero_ingresado)

if __name__ == "__main__":
    prueba()