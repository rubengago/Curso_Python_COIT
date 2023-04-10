'''
Incluye funciones para comprobar si:
- Un usuario ha incluido una cadena vacía en cualquiera de los valores requeridos.
- El ID se corresponde con un DNI, un NIE o no es un valor valido.
- La letra del DNI o el NIE se corresponde con la letra correspondiente
'''
from math import floor

LONGITUD_ID = 9    # Un DNI tiene 9 caracteres: 8 digitos + 1 letra de control
letra_control = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
                 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
primera_letra_NIE = ['X', 'Y', 'Z']        # Un NIE solo puede comenzar por X, Y o Z

def isEmpty(in_text: str) -> bool:
    '''
    Comprueba si el usuario ha introducido algun valor o la cadena esta vacia
    :param in_value: cadena de caracteres
    :return: Verdadero si la cadena esta vacia, falso si contiene algun valor
    '''
    try:
        if not in_text:
            raise ValueError("La cadena está vacía")
        return False
    except ValueError as e:
        print(e)
        return True


def idCheck(id: str) -> int:
    '''
    Función que evalua si el DNI/NIE introducido se corresponde con un valor válido para este tipo de documentos
    :param id: Cadena de caracteres que representa el DNI/NIE
    :return: Devuelve 0 si es un DNI, 1 si es un NIE y 2 si no es valor correcto para ninguno de los dos documentos
    '''
    try:
        if len(id) == LONGITUD_ID and id[:LONGITUD_ID - 1].isdigit() and id[LONGITUD_ID - 1].isalpha():
            '''
            La condicion que debe cumplir a priori una cadena que simule un DNI es que:
            i. Tenga 9 caracteres
            ii. Los 8 primeros sean digitos (0-9)
            iii. El ultimo valor de la cadena se corresponda con un caracter alfabetico
            En caso de ser así, validamos que la letra de control se corresponda con lo marcado en el algoritmo para el
            calculo de dicha letra 
            (https://www.interior.gob.es/opencms/ca/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/)
            '''
            dni_num = int(id[:LONGITUD_ID - 1])
            if id[LONGITUD_ID - 1].upper() == letra_control[dni_num - 23 * floor(dni_num / 23)]:
                return 0
            else:
                raise ValueError("El codigo para el documento de identificación no se corresponde con un valor correcto.")
        elif len(id) == LONGITUD_ID and id[0].upper() in primera_letra_NIE and id[1:LONGITUD_ID - 1].isdigit() \
                and id[LONGITUD_ID - 1].isalpha():
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
                return 1
            else:
                raise ValueError("El codigo para el documento de identificación no se corresponde con un valor correcto.")
        else:
            raise ValueError("El codigo para el documento de identificación no se corresponde con un valor correcto.")
    except ValueError as error:
        print(error)
        return 2
