# Defino la tupla con los meses del año por orden (de Enero a Diciembre) como una constante (los valores no cambian).
MESES_ANYO = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

valor_entrada = input("Indique el número de mes a mostrar (1 - Enero...12 - Diciembre): ")
'''
Chequeo que el valor sea un entero mayor o igual que 1 Y menor o igual que 12
En caso contrario, muestro un mensaje de error.
'''
if valor_entrada.isdigit() and int(valor_entrada) >= 1 and int(valor_entrada) <= 12:
    print(MESES_ANYO[int(valor_entrada) - 1])
else:
    print("El valor introducido no es correcto.")
