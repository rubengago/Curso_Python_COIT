# Los lados de un triangulo deben ser valores valores float positivos mayores que 0
lado1 = input("Introduzca un valor para el primer lado del triangulo: ")
lado2 = input("Introduzca un valor para el segundo lado del triangulo: ")
lado3 = input("Introduzca un valor para el tercer lado del triangulo: ")

# Rutina que comprueba si una cadena dada se corresponde o no con un valor de tipo 'float'
def isFloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

''' 
Comprobamos que los valores introducidos se corresponden con los valores esperados (float mayores que 0)
En caso contrario, mostramos mensaje de error
'''
if isFloat(lado1) and float(lado1) > 0 and \
        isFloat(lado2) and float(lado2) > 0 \
        and isFloat(lado3) and float(lado3) > 0:
    if float(lado1) == float(lado2) \
            and float(lado1) == float(lado3):
        print("El triángulo de lados", lado1, ",", lado2, "y", lado3, ", es un triángulo equilátero.")
    elif float(lado1) != float(lado2) \
            and float(lado1) != float(lado3) \
            and float(lado2) != float(lado3):
        print("El triángulo de lados", lado1, ",", lado2, "y", lado3, ", es un triángulo escaleno.")
    else:
        print("El triángulo de lados", lado1, ",", lado2, "y", lado3, ", es un triángulo isósceles.")
else:
    print("Los valores introducidos no son correctos.")
    exit(1)
