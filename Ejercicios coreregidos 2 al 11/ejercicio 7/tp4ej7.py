################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 5: Restas sucesivas

def division_lenta(dividendo,divisor):
    cociente=0
    resto=0
    while dividendo>=divisor:
        dividendo -= divisor
        resto= dividendo
        cociente+=1
    return(cociente,resto)

def prueba():
    numerador = int(input("Ingrese un numerador: "))
    denominador= int(input("Ingrese un denominador: "))
    resultado=division_lenta(numerador,denominador)
    print(resultado)

if __name__ == "__main__":
    prueba()