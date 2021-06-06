################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 4: Comparacion de numeros

def compara(numero1,numero2):
    if numero1<numero2:
        print("-1")
    elif numero1>numero2:
        print("1")
    else:
        print("0")
while True:
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese un segundo numero: "))
    compara(n1,n2)

def prueba():
    pass

if __name__ == "__main__":
    prueba()