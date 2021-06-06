################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 5: Positivos y Negativos

def prueba():
    pass

def signo(numero):
    if numero>0:
        print("Numero positivo")
    elif numero<0:
        print("Numero negativo")
    else:
        print("El numero ingresado es cero")

while True:
    numero_ingresado = float(input("Ingrese un numero para verificar su signo: "))
    signo(numero_ingresado)   

if __name__ == "__main__":
    prueba()