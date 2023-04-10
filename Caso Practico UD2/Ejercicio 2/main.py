import check_inputs
from getpass import getuser
'''
Creo una variable a la ruta del documento teniendo en cuenta al usuario local que esta ejecutando el prorgrama
'''
path = "C:/Users/" + getuser() + "/Documents/personas.txt"
datos_persona = [] # Creo una lista vacía con los datos de una persona que ire agreando segun se incluyan
'''
Solicito el nombre y apellidos de la persona y verifico (en cada caso que):
1. Que la cadena tecleada no esté vacía
2. Que los valores se correspondan con caracteres alfabeticos (de la A a la Z, en mayusuculas o minusculas).
En caso de que alguno de estos dos casos se de, se volverá a solicitar un valor al usuario hasta que sea correcto.
'''
nombre = input("Introduzca el nombre de la persona: ")
while check_inputs.isEmpty(nombre) or not(nombre.isalpha()):
    nombre = input("Introduzca el nombre de la persona: ")
# Añado el nombre a la lista de los datos de la persona
datos_persona.append(nombre)


apellido1 = input("Introduzca el primer apellido de la persona: ")
while check_inputs.isEmpty(apellido1) or not(apellido1.isalpha()):
    apellido1 = input("Introduzca el primer apellido de la persona: ")
# Añado el primer apellido a la lista de los datos de la persona
datos_persona.append(apellido1)

apellido2 = input("Introduzca el segundo apellido de la persona: ")
while check_inputs.isEmpty(apellido2) or not(apellido2.isalpha()):
    apellido2 = input("Introduzca el segundo apellido de la persona: ")
# Añado el segundo apellido a la lista de los datos de la persona
datos_persona.append(apellido2)

'''
Pido al usuario que introduzca un DNI/NIE de manera que:
1. No teclee una cadena vacía
2. EL DNIE/NIE se corresponda con un formato valido ( 8 digitos + letra de control para el DNI 
y una letra (X/Y/Z) + 7 digitos + 1 letra de control para el NIE
Se pedirá al usuario que introduzca un valor hasta que ambas condiciones se den.
'''
documento_identidad = input("Introduzca el DNI/NIE de la persona: ")
while check_inputs.isEmpty(documento_identidad) or check_inputs.idCheck(documento_identidad) == 2:
    documento_identidad = input("Introduzca el DNI/NIE de la persona: ")
# Añado el DNI/NIE a la lista de los datos de la persona
datos_persona.append(documento_identidad)

'''
Escribo los datos en fichero y me aseguro de manejar los errores relativos a:
1. Ruta del archivo incorrecta
2. Permisos insuficientes para escritura
3. Otros
'''
try:
    file = open(path,"w")
    file.write(nombre + "\n")
    file.write(apellido1 + "\n")
    file.write(apellido2 + "\n")
    file.write(documento_identidad + "\n")
except FileNotFoundError:
    print("Por favor, compruebe que la ruta del documento sea correcta.")
except PermissionError:
    print("Por favor, revise que su usuario tiene permisos de escritura en el documento.")
except Exception as e:
    print("Ha ocurrido un error: ", type(e))
else:
    file.close()

'''
Realizo la lectura de los datos del fichero para asegurarme que sean los mismos que los introducidos 
(guardados en la lista datos_person). Manejo excepciones para errores de tipo:
1. Ruta del archivo incorrecta
2. Permisos insuficientes para escritura
3. Los valores del fichero no son iguales a los de la lista de datos_persona
4. Otros
'''
try:
    file = open(path, "r")
    '''
    Leo las lineas del fichero y las almaceno en una lista
    '''
    contenido = file.readlines()
    # Ambas listas deben tener el mismo número de elementos. En caso contrario, ha habido un error al escribir en el fichero
    if len(datos_persona) != len(contenido):
        raise ValueError("Error en la escritura del fichero. Los datos no coinciden con los introducidos.")
    else:
        '''
        Valido elemento a elemento que coincidan en ambas listas.
        Elimino el ultimo caracter en los elementos leidos del fichero, por el caracter de salto de linea.
        '''
        for i in range(len(datos_persona)):
            aux = contenido[i]
            if datos_persona[i] != aux[:len(contenido[i]) - 1]:
                raise ValueError("Error en la escritura del fichero. Los datos no coinciden con los introducidos.")
except FileNotFoundError:
    print("Por favor, compruebe que la ruta del documento sea correcta.")
except PermissionError:
    print("Por favor, revise que su usuario tiene permisos de escritura en el documento.")
except ValueError as error:
    print(error)
except Exception as exception:
    print("Ha ocurrido un error: ", type(exception))
else:
    file.close()
    print("Los datos del fichero coinciden con los tecleados.")
finally:
    print("Hasta pronto.")
