import unittest

from Persona import Persona

class UnitaryTest(unittest.TestCase):

    def test_mayor_edad_1(self):
        # Realizamos caso de prueba 1 (ver archivo Casos de Prueba)
        persona = Persona("Juan", "Gomez", -10)
        self.assertEqual("Error. El valor de la edad de la persona no es correcta.", persona.mayoria_edad())

    def test_mayor_edad_2(self):
        # Realizamos caso de prueba 2 (ver archivo Casos de Prueba)
        persona = Persona("Juan", "Gomez", 0)
        self.assertEqual(False, persona.mayoria_edad())

    def test_mayor_edad_3(self):
        # Realizamos caso de prueba 3 (ver archivo Casos de Prueba)
        persona = Persona("Juan", "Gomez", 10)
        self.assertEqual(False, persona.mayoria_edad())

    def test_mayor_edad_4(self):
        # Realizamos caso de prueba 4 (ver archivo Casos de Prueba)
        persona = Persona("Juan", "Gomez", 17)
        self.assertEqual(False, persona.mayoria_edad())

    def test_mayor_edad_5(self):
        # Realizamos caso de prueba 5 (ver archivo Casos de Prueba)
        persona = Persona("Juan", "Gomez", 18)
        self.assertEqual(True, persona.mayoria_edad())

    def test_mayor_edad_6(self):
        # Realizamos caso de prueba 5 (ver archivo Casos de Prueba)
        persona = Persona("Juan", "Gomez", 79)
        self.assertEqual(True, persona.mayoria_edad())

if __name__ == 'main':
    unittest.main()
