def convertir_gramos (in_peso:float)->float:
    '''
    Función que devuelve el equivalente en gramos de la cantidad introducida
    :param in_peso: Cantidad en kilogramos a convertir
    :return: Total de gramos equivalente
    '''
    return in_peso * 1000

def convertir_toneladas (in_peso:float)->float:
    '''
    Función que devuelve el equivalente en toneladas de la cantidad introducida
    :param in_peso: Cantidad en kilogramos a convertir
    :return: Total de toneladas equivalente
    '''
    return in_peso / 1000

def convertir_onza (in_peso:float)->float:
    '''
    Función que devuelve el equivalente en onzas de la cantidad introducida
    :param in_peso: Cantidad en kilogramos a convertir
    :return: Total de onzas equivalente (peso Kilogramo * 35.274)
    '''
    return in_peso * 35.274
