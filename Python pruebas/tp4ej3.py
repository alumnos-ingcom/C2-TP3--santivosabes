################
# Santiago Almonacid - @santivosabes
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Ejercicio 3: Conversion de temperaturas

def conversion_a_farenheit(grados_centigrados):
    farenheit=((grados_centigrados*9/5)+32)
    return farenheit
def conversion_a_centigrados(grados_farenheit):
    centigrados=((grados_farenheit-32)*5/9)
    return centigrados
while True:
    seleccion=int(input("Elija 1 para convertir de Cº a Fº, cualquier numero para convertir de Fº a Cº: "))
    if seleccion==1:
        cent = float(input("Ingrese un numero en Grados Centigrados: "))
        resultado=conversion_a_farenheit(cent)
        print(resultado)
    else:
        fare=float(input("Ingrese un numero en Grados Farenheit: "))
        resultado=conversion_a_centigrados(fare)
        print(resultado)