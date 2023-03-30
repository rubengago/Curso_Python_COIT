cadena_entrada = input("Introduzca una cadena de caracteres: ")

# Verifico que la longitud sea mayor que 3

if len(cadena_entrada) >= 3:
    print(cadena_entrada[:3])
else:
    print("La cadena debe tener una longitud mayor o igual a 3 caracteres.")
    exit(1)
