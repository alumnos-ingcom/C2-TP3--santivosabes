################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 9: Numeros primos

def primo(numero):
    for x in range(2,numero):
        if numero% x == 0:
            #print("No es primo")
            return False
    #print("Es primo")
    return True
   
def prueba():
    while True:
        numero_ingresado=int(input("Ingrese un numero para verificar si es primo o no: "))
        primo(numero_ingresado)
        if primo==False:
            print("No es primo")
        else:
            print("Es primo")

if __name__ == "__main__":
    prueba()