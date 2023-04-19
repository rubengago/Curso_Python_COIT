import string

class Clinica:

    '''
    Defino un atributo de clase con los caracteres validos para el codigo, poblacion
    '''
    caracteres_codigo_clinica = string.ascii_lowercase + ' ' + '-' + string.digits
    caracteres_poblacion_clinica = string.ascii_lowercase + ' ' + '-'
    caracteres_provincia_clinica = string.ascii_lowercase + ' '
    def __init__(self, codigo, poblacion, provincia, cantidad_camas):
        self.__codigo = codigo
        self.__poblacion = poblacion
        self.__provincia = provincia
        self.__cantidad_camas = cantidad_camas
        self.__camas_ocupadas = 0
        self.__plantilla_medicos = []

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        '''
        El codigo de la clinica solo puede tener los siguientes tipos de caracteres:
        - Alfabeticos (letras de la A a la Z)
        - Espacio en blanco
        - Guion
        - Numeros
        '''
        try:
            if codigo == "":
                raise ValueError("El codigo de la clinica no puede ser una cadena vacía.")
            else:
                for char in codigo.lower:
                    if not (char in Clinica.caracteres_codigo_clinica):
                        raise TypeError("El valor del codigo de la clinica no es correcto. Introduzca un codigo"
                                         "con una combinación de súimbolos de los siguientes tipos:\n"
                                         "- Letras\n"
                                         "- Números\n"
                                         "- Espacio en blanco\n"
                                         "- Guión")
                self.__codigo = codigo

        except ValueError as e1:
            print(e1)
        except TypeError as e2:
            print(e2)

    @property
    def poblacion(self):
        return self.__poblacion

    @poblacion.setter
    def poblacion(self, poblacion):
        '''
            El valor de la poblacion de la clinica solo puede tener los siguientes tipos de caracteres:
            - Alfabeticos (letras de la A a la Z)
            - Espacio en blanco
            - Guion
        '''
        try:
            if poblacion == "":
                raise ValueError("La poblacion de la clinica no puede ser una cadena vacía.")
            else:
                for char in poblacion.lower():
                    if not (char in Clinica.caracteres_poblacion_clinica):
                        raise TypeError("El valor del codigo de la clinica no es correcto. Introduzca un codigo"
                                        "con una combinación de súimbolos de los siguientes tipos:\n"
                                        "- Letras\n"
                                        "- Espacio en blanco\n"
                                        "- Guion")
                self.__poblacion = poblacion

        except ValueError as e1:
            print(e1)
        except TypeError as e2:
            print(e2)

    @property
    def provincia(self):
        return self.__provincia

    @provincia.setter
    def provincia(self, provincia):
        '''
            El valor de la provincia de la clinica solo puede tener los siguientes tipos de caracteres:
            - Alfabeticos (letras de la A a la Z)
            - Espacio en blanco
        '''
        try:
            if provincia == "":
                raise ValueError("La provincia de la clinica no puede ser una cadena vacía.")
            else:
                for char in provincia.lower():
                    if not (char in Clinica.caracteres_provincia_clinica):
                        raise TypeError("El valor del codigo de la clinica no es correcto. Introduzca un codigo"
                                         "con una combinación de súimbolos de los siguientes tipos:\n"
                                         "- Letras\n"
                                         "- Espacio en blanco\n")
                self.__provincia = provincia

        except ValueError as e1:
            print(e1)
        except TypeError as e2:
            print(e2)


    @property
    def cantidad_camas(self):
        return self.__cantidad_camas

    @cantidad_camas.setter
    def cantidad_camas(self, cantidad_camas):
        '''
        Cantidad de camas solo puede tomar un valor entero mayor que 0.
        Se entiende que el usuario introducirá el valor por consola, con lo cual será tratado como una cadena de caracteres
        '''
        try:
            if cantidad_camas == "":
                raise ValueError("La provincia de la clinica no puede ser una cadena vacía.")
            elif not cantidad_camas.isdigit() or int(cantidad_camas) < 0:
                raise TypeError ("El valor para la cantidad de camas no se corresponde con un valor esperado."
                                 "La cantidad de camas debe ser un entero mayor que 0.")
            else:
                self.__cantidad_camas = int(cantidad_camas)
        except ValueError as e1:
            print(e1)
        except TypeError as e2:
            print(e2)


    @property
    def camas_ocupadas(self):
        return self.__camas_ocupadas

    @camas_ocupadas.setter
    def camas_ocupadas(self, camas_ocupadas):

        '''
        Camas ocupadas solo puede tomar un valor entero mayor o igual que 0.
        Se entiende que el usuario introducirá el valor por consola, con lo cual será tratado como una cadena de caracteres
        '''
        try:
            if camas_ocupadas == "":
                raise ValueError("El valor de camas ocupadas no puede estar vacío.")
            elif not camas_ocupadas.isdigit() or int(camas_ocupadas) <= 0:
                raise TypeError("El valor para la camas ocupadas no se corresponde con un valor esperado."
                                "La cantidad de camas ocupadas debe ser un entero mayor o igual que 0.")
            else:
                self.__camas_ocupadas = int(camas_ocupadas)
        except ValueError as e1:
            print(e1)
        except TypeError as e2:
            print(e2)

    @property
    def plantilla_medicos(self):
        return self.__plantilla_medicos

    @plantilla_medicos.setter
    def plantilla_medicos(self, plantilla_medicos):
        self.__plantilla_medicos = plantilla_medicos


    def disponibilidad_camas(self):
        if self.__camas_ocupadas < self.__cantidad_camas:
            return True
        else:
            return False

    def plantilla_especialidad (self, especialidad: str):
        '''
        Metodo que devuelve la lista de medico de la especialidad indicada
        :param especialidad:
        :return: devuelve una lista vacía si no hay medicos de la especialidad dada, o con los diferentes
        medicos que sean de la misma especialidad que la especificada.
        '''
        lista_especialistas = []
        # Si la plantilla de medicos esta vacía, devuelvo la lista vacía.
        if len(self.__plantilla_medicos) > 0:
            for medico in self.__plantilla_medicos:
                if medico.especialidad.lower() == especialidad.lower():
                    lista_especialistas.append(medico)

        return lista_especialistas

    def ingreso_paciente(self):
        try:
            if self.__camas_ocupadas >= self.__cantidad_camas:
                raise Exception("La clinica no tiene cama disponibles.")
            else:
                self.__camas_ocupadas += 1
        except Exception as e:
            print(e)

    def ocupacion_clinica(self):
        return (self.__camas_ocupadas * 100) / self.__cantidad_camas

    def aniadir_medico(self, medico):
        self.__plantilla_medicos.append(medico)
