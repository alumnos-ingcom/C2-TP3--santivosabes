################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 2: Suma Lenta

def suma_lenta(n1=0,n2=0):
    for suma in range (n2):
        n1=n1+1
    return n1
    
def prueba():
    numero1= int(input("Ingrese numero 1: "))
    numero2= int(input("ingrese numero 2: "))
    c=0
    suma=suma_lenta(numero1,numero2)
    print(suma)

if __name__ == "__main__":
    prueba()