################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#Ejercicio 1: Ingreso de números enteros 
       
def ingreso_rango(numeros,valor_min=0,valor_max=100):
    try:
        if int(numeros)>=valor_min and int(numero)<=valor_max:
            return numeros
    except ValueError:
        return False
   
def ingreso_entero(mensaje):
    try:
        int(mensaje)
        return True
    except ValueError:
        return False
    
reintento=5
while reintento>0:
    numero = input("Ingrese un número: ")
    if ingreso_entero(numero):
        if ingreso_rango(numero):
            print("El numero ingresado es válido")
        else:
            print("El numero ingresado se pasa del rango")
            reintento=reintento-1
            print("Quedan ",reintento," reintentos disponibles")
    else:
        print("El numero ingresado no es válido")
        reintento=reintento-1
        print("Quedan ",reintento," reintentos disponibles")
print("Se quedo sin reintentos")
 

           
    
        

        