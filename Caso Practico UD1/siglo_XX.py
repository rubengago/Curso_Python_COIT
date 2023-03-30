valor_entrada = input("Introduzca el año a verificar: ")
'''
Compruebo que la cadena se corresponde con un valor entero positivo.
En caso contrario, se muestra un mensjae de error por pantalla.
'''
if valor_entrada.isdigit():
    anyo = int(valor_entrada)
    # Compruebo que el año se corresponda con el siglo 20 (comprende los años desde 1901 al 2000).
    if anyo < 1901 or anyo > 2000:
        print("El año", anyo, "no pertenece al siglo 20.")
    else:
        print("El año", anyo, "pertenece al siglo 20.")
else:
    print("El valor introducido no se corresponde con un valor de año correcto.")
    exit(1)
