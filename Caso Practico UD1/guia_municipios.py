diccionario_municipios = {"28001":"Madrid", "08001": "Barcelona", "46001":"Valencia",
                          "48001":"Bilbao", "41001":"Sevilla"}

'''
Consideraciones tomadas para el ejercicio:
1. El codigo postal solo puede contener valores numericos
2. Debe ser un valor con 5 digitos
'''

codigo_postal = input("Introduzca un valor para el codigo postal a consultar: ")
if codigo_postal.isdigit() and len(codigo_postal) == 5:
    if codigo_postal in diccionario_municipios:
        print("EL municipio que corresponde al codigo postal " + codigo_postal + " es "
              + diccionario_municipios[codigo_postal])
    else:
        print("El codigo postal introducido no se corresponde con ningun municipio.")
else:
    print("El codigo postal introducido no es correcto.")
