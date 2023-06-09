# Declaro como 'constante' el número de alumnos
NUM_ALUMNOS = 10
# Inicializo el contado de aprobados
num_aprobados = 0

# Rutina que comprueba si una cadena dada se corresponde o no con un valor de tipo 'float'
def isFloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

# Bucle para solicitar las notas de los 10 alumnos
for i in range(NUM_ALUMNOS):
    input_text="Introduzca un valor para la nota del alumno " + str(i + 1) + ": "
    nota = input(input_text)
    '''
    Chequeo que el valor introducido sea un valor de tipo float y con un valor entre 0 y 10. 
    En caso contrario muestro mensaje de error
    '''
    if isFloat(nota) and float(nota)>=0 and float(nota)<=10:
        # Valido si la nota se corresponde con un aprobado o no
        if float(nota) >= 5:
            num_aprobados += 1
    else:
        print("El valor introducido para la nota del alumno", i + 1, "no es correcto.")
        exit(1)

print("El numero de alumnos aprobados es de", num_aprobados)
# El numero de suspensos sera la diferencia entre el numero total de alumnos y el numero de aprobados
print("El numero de alumnos suspensos es de", NUM_ALUMNOS - num_aprobados)
