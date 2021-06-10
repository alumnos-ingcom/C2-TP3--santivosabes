################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 10: Factores primos

def factores_primos(numero):
    primos_hallados = []
    for i in range(2,numero+1):
        while numero%i==0:
            primos_hallados.append(i)
            numero=numero/i
    return primos_hallados

def prueba():
    while True:
        numeros=int(input("Ingrese un numero para verificar sus factores primos: "))
        resultado= factores_primos(numeros)
        print(resultado)
   
if __name__ == "__main__":
    prueba()