################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 8: Ordenar 3 valores

def prueba():
    pass

def mayor_a_menor(listas):
    listas.sort(reverse=True)
    print("De mayor a menor: ",listas)
def menor_a_mayor(listas):
    listas.sort()
    print("De menor a mayor: ",listas)
    pass
 
lista = [] 
for x in range (3):
    numeros=int(input("Ingrese 3 numeros para ordenarlos:"))
    lista.append(numeros)
mayor_a_menor(lista)
menor_a_mayor(lista)

if __name__ == "__main__":
    prueba()