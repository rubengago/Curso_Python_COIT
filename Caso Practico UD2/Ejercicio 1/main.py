import conversores.conversor_grados, conversores.conversor_pesos
from float_check import isFloat
'''
Declaro 3 listas:
1. Lista con opciones para realizar la conversión: P para convertir peso, T para convertir temperatura
2. Lista con las posibles alternativas de medidas de peso: g para gramos, t para toneladas y o para onzas.
3. Lista con los posibles valores de unidades de temperatura: F para Fahrenheit y K para Kelvin.
'''
opciones_conversion = ['P', 'T']
medidas_peso = ['g', 't', 'o']
medidas_temperatura = ['F', 'K']

'''
Solicito al usuario si desea convertir un valor de peso o un valor de temperatura.
Se solicitará hasta que el usuario introduzca un valor valido.
'''
opcion = input("Confirme si desea convertir peso (P) o temperatura (T): ")
while opcion.upper() not in opciones_conversion:
    opcion = input("Confirme si desea convertir peso (P) o temperatura (T): ")

if opcion.upper() == opciones_conversion[0]:
    ''' 
    Pido al usuario que introduzca la cantidad en kilos a transformar.
    Se sigue solicitando hasta que el valor tecleado se corresponda con un valor de tipo real.
    '''
    peso_kilogramos = input("Introduzca la cantidad de kilogramos que desea convertir: ")
    while not isFloat(peso_kilogramos):
        peso_kilogramos = input("Introduzca la cantidad de kilogramos que desea convertir: ")
    ''' 
    Pido al usuario que introduzca la unidad a la que realizar la conversión.
    Se sigue solicitando hasta que el valor introducido se corresponda con una de las medidas definidas.
    '''
    unidad_conversion = input("Introduzca la unidad en la que quiere realizar la conversión"
                              "(g para gramos, t para toneladas y o para onzas): ")
    while unidad_conversion.lower() not in medidas_peso:
        unidad_conversion = input("Introduzca la unidad en la que quiere realizar la conversión"
                                  "(g para gramos, t para toneladas y o para onzas): ")
    if unidad_conversion == medidas_peso[0]:
        print(float(peso_kilogramos), "son", conversores.conversor_pesos.convertir_gramos(float(peso_kilogramos)),
              "gramos.")
    elif unidad_conversion == medidas_peso[1]:
        print(float(peso_kilogramos), "son", conversores.conversor_pesos.convertir_toneladas(float(peso_kilogramos)),
              "toneladas.")
    else:
        print(float(peso_kilogramos), "son", conversores.conversor_pesos.convertir_onza(float(peso_kilogramos)),
              "onzas.")
else:
    ''' 
    Pido al usuario que introduzca la cantidad en kilos a transformar.
    Se sigue solicitando hasta que el valor tecleado se corresponda con un valor de tipo real.
    '''
    temperatura = input("Introduzca la temperatura que desea convertir: ")
    while not isFloat(temperatura):
        temperatura = input("Introduzca la temperatura que desea convertir: ")
    ''' 
    Pido al usuario que introduzca la unidad a la que realizar la conversión.
    Se sigue solicitando hasta que el valor introducido se corresponda con una de las medidas definidas.
    '''
    unidad_conversion = input("Introduzca la unidad en la que quiere realizar la conversión"
                              "(F para grados Fahrenheit, K para grados Kelvin): ")
    while unidad_conversion.upper() not in medidas_temperatura:
        unidad_conversion = input("Introduzca la unidad en la que quiere realizar la conversión"
                                  "(F para grados Fahrenheit, K para grados Kelvin): ")
    if unidad_conversion == medidas_temperatura[0]:
        print(float(temperatura), "ºC son", conversores.conversor_grados.convertir_fahrenheit(float(temperatura)),
              "ºF.")
    else:
        print(float(temperatura), "ºC son", conversores.conversor_grados.convertir_kelvin(float(temperatura)),
              "ºK.")
