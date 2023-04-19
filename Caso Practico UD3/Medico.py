from Persona import Persona
import string

class Medico(Persona):

    '''
    Defino un atributo de clase con los caracteres que puede tomar como valor la especialidad (letras y espacio en blanco)
    '''
    caracteres_especialidad = string.ascii_lowercase + ' '
    def __init__(self, dni, nombre, apellidos, edad, numero_colegiado, especialidad):
        super().__init__(dni, nombre, apellidos, edad)
        self.__numero_colegiado = numero_colegiado
        self.__especialidad = especialidad

    @property
    def numero_colegiado(self):
        return self.__numero_colegiado

    @numero_colegiado.setter
    def numero_colegiado(self, numero_colegiado):
        '''
        El numero de colegiado tendrá un valor que será una cadena de caracteres alfanumericos.
        En caso de no ser asi, se mostrará un mensaje de error.
        '''
        try:
            if numero_colegiado == "":
                raise ValueError("El número de colegiado no puede ser una cadena vacía.")
            elif not numero_colegiado.isalnum():
                raise TypeError("El valor para el número de colegiado solo puede contener caracteres:\n"
                                "- Alfabeticos (de la 'A' a la 'Z')\n"
                                "- Numéricos")
            else:
                self.__numero_colegiado = int(numero_colegiado)
        except ValueError as e1:
            print(e1)
        except TypeError as e2:
            print(e2)


    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, especialidad):

        '''
        La especialidad sera una cadena de caracteres alfabeticos y con espacios en blanco.
        '''
        try:
            if especialidad == "":
                raise ValueError("El número de colegiado no puede ser una cadena vacía.")
            else:
                for char in especialidad.lower():
                    if char not in Medico.caracteres_especialidad:
                        raise TypeError("La especialidad debe tener un valor que incluya caracteres de tipo: \n"
                                        "- Alfabeticos (letras de la 'A' a la 'Z'\n"
                                        "- Espacio en Blanco")

                self.__especialidad = especialidad
        except ValueError as e1:
            print(e1)
        except TypeError as e2:
            print(e2)
