# Defino la 'constante' del numero de dias en una semana
NUM_DIAS_SEMANA = 7
# Creo una tupla con los nombres de los diferentes dias de la semana
dias_semana=("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
# Inicializo la variable del total de ventas semanal
total_ventas_semanal = 0

def isFloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

# Bucle que recorre la tupla
for dia in dias_semana:
    input_text = "Introduzca la venta del " + dia + ": "
    venta_diaria = input(input_text)
    '''
    Valido que el valor introducido sea un float positivo (mayor o igual que 0). 
    En caso negativo, muestro mensaje de error.
    '''
    if isFloat(venta_diaria) and float(venta_diaria) >= 0:
        total_ventas_semanal += float(venta_diaria)
    else:
        print("El valor para la venta del " + dia + " no es correcto.")
        exit(1)

venta_semanal_media = total_ventas_semanal / NUM_DIAS_SEMANA
print("La media de la venta en la semana ha sido de:", venta_semanal_media, "€")
