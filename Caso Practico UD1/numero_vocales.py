# Defino la cadena 'Supercalifragilisticoespialidoso' como 'constante'
TEXTO = "Supercalifragilisticoespialidoso"
# Inicializo la variable para el recuento de vocales
numero_vocales = 0
'''
Convierto la cadena en mayusculas
Esto ayudaria en caso de que la cadena tuviera alguna vocal en mayuscula
'''
aux = TEXTO.upper()

for letra in aux:
    if letra =='A' or letra =='E' or letra =='I' or letra =='O' or letra =='U':
        numero_vocales += 1

print("El número de vocales que hay en '" + TEXTO + "' son", numero_vocales, ".")
