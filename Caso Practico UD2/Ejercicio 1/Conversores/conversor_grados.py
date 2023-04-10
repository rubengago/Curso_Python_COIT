def convertir_fahrenheit (in_temp):
    '''
    Convierte en grados fahrenheit la temperatura en ºC que se pasa como parametro.
    La formula de conversion es Temp en ºF = Temp en ºC * 1,8 + 32
    :param in_temp: Temperatura en grados Celsius
    :return: Temperatura en grados Fahrenheit equivalente
    '''
    return in_temp * 1.8 + 32

def convertir_kelvin (in_temp):
    '''
    Convierte en grados fahrenheit la temperatura en ºC que se pasa como parametro.
    La formula de conversion es Temp en ºK = ºC + 273.15
    :param in_temp: Temperatura en grados Celsius
    :return: Temperatura en grados Kelvin equivalente
    '''
    return in_temp + 273.15
