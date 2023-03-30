'''Los lados de un triangulo deben ser valores enteros positivos'''
valor_entrada1 = input("Introduzca un valor para el primer lado del triangulo: ")
valor_entrada2 = input("Introduzca un valor para el segundo lado del triangulo: ")
valor_entrada3 = input("Introduzca un valor para el tercer lado del triangulo: ")

''' 
Comprobamos que los valores introducidos se corresponden con los valores esperados (enteros positivos)
En caso contrario, mostramos mensaje de error
'''
if valor_entrada1.isdigit() and valor_entrada2.isdigit() and valor_entrada3.isdigit():
    lado1, lado2, lado3 = int(valor_entrada1), int(valor_entrada2), int(valor_entrada3)
    if lado1 == lado2 and lado1 == lado3:
        print("El triángulo de lados", lado1, ",", lado2, "y", lado3, ", es un triángulo equilátero.")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("El triángulo de lados", lado1, ",", lado2, "y", lado3, ", es un triángulo escaleno.")
    else:
        print("El triángulo de lados", lado1, ",", lado2, "y", lado3, ", es un triángulo isósceles.")
else:
    print("Los valores introducidos no son correctos.")
    exit(1)
