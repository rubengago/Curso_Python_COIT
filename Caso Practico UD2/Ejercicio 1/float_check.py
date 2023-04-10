def isFloat(in_value:str)->bool:
    '''
    Funcion que evalua si una cadena se corresponde con un valor de tipo float
    :param in_value: cadena de entrada
    :return: valor booleano (verdadero si se corresponde con un float, falso si no)
    '''
    try:
        float(in_value)
        return True
    except ValueError:
        return False
