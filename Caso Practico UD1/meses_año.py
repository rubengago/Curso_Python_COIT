# Defino la tupla con los meses del año por orden (de Enero a Diciembre) como una constante (los valores no cambian).
MESES_ANYO = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

numero_mes = input("Indique el número de mes a mostrar (1 - Enero...12 - Diciembre): ")
'''
Chequeo que el valor sea un entero mayor o igual que 1 Y menor o igual que 12
En caso contrario, muestro un mensaje de error.
'''
if numero_mes.isdigit() and int(numero_mes) >= 1 and int(numero_mes) <= 12:
    print("El valor introducido se corresponde con el mes de " + MESES_ANYO[int(numero_mes) - 1] +".")
else:
    print("El valor introducido no es correcto.")
