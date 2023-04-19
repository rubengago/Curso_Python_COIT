import string
from math import floor

LONGITUD_ID = 9    # Un DNI tiene 9 caracteres: 8 digitos + 1 letra de control
letra_control = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
                 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
primera_letra_NIE = ['X', 'Y', 'Z']        # Un NIE solo puede comenzar por X, Y o Z
class Persona:
    '''
    Defino un atributo de clase con los caracteres que puede tomar como valor:
    - el nombre: alfabeticos + espacio en blanco
    - los apellidos: alfabeticos + espacio en blanco + guion
    '''
    caracteres_nombre = string.ascii_lowercase + ' '
    caracteres_apellidos = caracteres_nombre + '-'
    def __init__(self, dni, nombre, apellidos, edad):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        try:
            if len(dni) == LONGITUD_ID and dni[:LONGITUD_ID - 1].isdigit() and dni[LONGITUD_ID - 1].isalpha():
                '''
                La condicion que debe cumplir a priori una cadena que simule un DNI es que:
                i. Tenga 9 caracteres
                ii. Los 8 primeros sean digitos (0-9)
                iii. El ultimo valor de la cadena se corresponda con un caracter alfabetico
                En caso de ser así, validamos que la letra de control se corresponda con lo marcado en el algoritmo para el
                calculo de dicha letra 
                (https://www.interior.gob.es/opencms/ca/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/)
                '''
                dni_num = int(dni[:LONGITUD_ID - 1])
                if dni[LONGITUD_ID - 1].upper() == letra_control[dni_num - 23 * floor(dni_num / 23)]:
                    self.__dni = dni
                else:
                    raise ValueError(
                        "El codigo para el documento de identificación no se corresponde con un valor correcto.")
            elif len(dni) == LONGITUD_ID and dni[0].upper() in primera_letra_NIE and dni[1:LONGITUD_ID - 1].isdigit() \
                    and dni[LONGITUD_ID - 1].isalpha():
                '''
                La condicion que debe cumplir a priori una cadena que simule un DNI es que:
                i. Tenga 9 caracteres
                ii. Los 8 primeros sean digitos (0-9)
                iii. El ultimo valor de la cadena se corresponda con un caracter alfabetico
                En caso de ser así, validamos que la letra de control se corresponda con lo marcado en el algoritmo para el
                calculo de dicha letra 
                (https://www.interior.gob.es/opencms/ca/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/)
                '''

                nie_num = int(str(ord(NIE[0].upper()) - ord("X")) + NIE[1:LONGITUD_ID - 1])
                if id[LONGITUD_ID - 1].upper() == letra_control[nie_num - 23 * floor(nie_num / 23)]:
                    self.__dni = dni
                else:
                    raise ValueError(
                        "El codigo para el documento de identificación no se corresponde con un valor correcto.")
            else:
                raise ValueError(
                    "El codigo para el documento de identificación no se corresponde con un valor correcto.")
        except ValueError as error:
            print(error)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        '''
        El nombre solo puede tomar valores alfabeticos o el espacio en blanco.
        En caso de no ser asi, se mostrará un mensaje de error
        '''
        try:
            if nombre == "":
                raise ValueError("El nombre no puede corresponderse con una cadena vacía.")
            else:
                for char in nombre.lower():
                    if char not in Persona.caracteres_nombre:
                        raise TypeError("El valor del nombre no es correcto. Introduzca un nombreo"
                                        "con una combinación de caracteres de los siguientes tipos:\n"
                                        "- Letras\n"
                                        "- Espacio en blanco\n"
                                        "- Guion")
                self.__nombre = nombre
        except ValueError as e1:
            print(e1)
        except TypeError as e2:
            print(e2)

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        '''
        El nombre solo puede tomar valores alfabeticos o el espacio en blanco.
        En caso de no ser asi, se mostrará un mensaje de error
        '''
        try:
            if apellidos == "":
                raise ValueError("Los apellidos no pueden ser una cadena vacía.")
            else:
                for char in apellidos.lower():
                    if char not in Persona.caracteres_nombre:
                        raise TypeError("El valor de los apellidos no es correcto. Introduzca los apellidos"
                                        "con una combinación de caracteres de los siguientes tipos:\n"
                                        "- Letras\n"
                                        "- Espacio en blanco\n"
                                        "- Guion")
                self.__apellidos = apellidos
        except ValueError as e1:
            print(e1)
        except TypeError as e2:
            print(e2)

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        '''
        La edad solo puede tomar un valor entero mayor o igual que 0.
        Se entiende que el usuario introducirá el valor por consola, con lo cual será tratado como una cadena de caracteres.
        '''
        try:
            if edad == "":
                raise ValueError("La edad no puede estar vacía.")
            elif not edad.isdigit() or int(edad) <= 0:
                raise TypeError("El valor para la edad no se corresponde con un valor esperado."
                                "La edad debe ser un entero mayor o igual que 0.")
            else:
                self.__edad = int(edad)
        except ValueError as e1:
            print(e1)
        except TypeError as e2:
            print(e2)


    def mayoria_edad(self):
        if self.__edad >= 18:
            return True
        elif self.__edad >= 0 and self.__edad < 18:
            return False
        else:
            return ("Error. El valor de la edad de la persona no es correcta.")
