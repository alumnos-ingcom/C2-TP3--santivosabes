################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 10: Factores primos

def prueba():
    pass
def descomposicion(numero):
    primos_hallados = []
    for i in range(2,numero+1):
        while numero%i==0:
            primos_hallados.append(i)
            numero=numero/i
    print(primos_hallados)

while True:
    numeros=int(input("Ingrese un numero para verificar sus factores primos: "))
    descomposicion(numeros)
            
if __name__ == "__main__":
    prueba()