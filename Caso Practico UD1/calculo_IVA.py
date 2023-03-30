# Declaro IVA del 21% como constante
IVA = 0.21

# Rutina que comprueba si una cadena se corresponde con un valor float o no
def isFloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

# Solicito un valor al usuario
importe = input("Introzuca el importe (para introducir un valor con decimales debe usar el punto como separador): ")

''' 
Reviso que el valor se corresponda con un float. En caso contrario, se muestra un mensaje de error
'''
if isFloat(importe):
    # Compruebo que el importe sea mayor que 0. Se entiende que el calculo no aplica para importes negativos
    if float(importe) > 0:
        iva_importe = float(importe) * IVA
        total = float(importe) + iva_importe
        print("El IVA para un importe de", float(importe), "€ es de", iva_importe, "€")
        print("El total (importe + IVA) corresponde a", total, "€")
    else:
        print("El importe introducido debe ser mayor que 0.")
        exit(1)
else:
    print("El valor introducido no es correcto.")
    exit(2)
