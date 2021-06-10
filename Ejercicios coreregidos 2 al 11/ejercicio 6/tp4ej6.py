################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 6: Maximo y minimo

def minimo(lista):
    print ("El minimo valor dentro de la lista es: ",min(lista))
      
def maximo(lista):
    print ("El mayor valor dentro de la lista es: ",max(lista))

def prueba():
    listas=[]
    for x in range (10):
        numeros=int(input("Ingrese 10 numeros para verificar mayor y menor: "))
        listas.append(numeros)
        print(listas)
    maximo(listas)
    minimo(listas)
    
if __name__ == "__main__":
    prueba()