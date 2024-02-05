"""
test_convert_numbers.py

Clase para implementar casos de prueba para la clase convertNumbers.py
"""
import unittest
import re
from convertNumbers import ConvertNumbers

class TestConvertNumbers(unittest.TestCase):
    """Clase para los casos de prueba"""

    def setUp(self):
        self.converter = ConvertNumbers("TC1.txt", "ConvertionResults.txt")
        self.generated_data = self.load_and_split_data('A4.2.P2.Results.txt')

    def load_and_split_data(self, file_name):
        """Carga de datos de Prueba 1"""
        with open(file_name, 'r', encoding='utf-8') as f:
            data = f.read()

        # Dividir los datos en función de las marcas "NUMBER TCX BIN HEX"
        split_data = re.split(r'NUMBER\tTC[1-4]\tBIN\tHEX', data)

        # Eliminar líneas vacías y espacios en blanco adicionales
        split_data = [line.strip() for line in split_data if line.strip()]

        return split_data

    def test_tc1(self):
        """Caso de Prueba 1"""
        converter = ConvertNumbers("TC1.txt", "ConvertionResults.txt")
        converter.process_file()

        test_data = self.generated_data[0].split('\n')
        validation = [linea for linea in converter.generated_data.split('\n') if linea]

        for i, line in enumerate(validation):
            self.assertEqual(line, test_data[i])

    def test_tc2(self):
        """Caso de Prueba 2"""
        converter = ConvertNumbers("TC2.txt", "ConvertionResults.txt")
        converter.process_file()

        test_data = self.generated_data[1].split('\n')
        validation = [linea for linea in converter.generated_data.split('\n') if linea]

        for i, line in enumerate(validation):
            self.assertEqual(line, test_data[i])

    def test_tc3(self):
        """Caso de Prueba 3"""
        converter = ConvertNumbers("TC3.txt", "ConvertionResults.txt")
        converter.process_file()

        test_data = self.generated_data[2].split('\n')
        validation = [linea for linea in converter.generated_data.split('\n') if linea]

        for i, line in enumerate(validation):
            self.assertEqual(line, test_data[i])

    def test_tc4(self):
        """Caso de Prueba 3"""
        converter = ConvertNumbers("TC4.txt", "ConvertionResults.txt")
        converter.process_file()

        test_data = self.generated_data[3].split('\n')
        validation = [linea for linea in converter.generated_data.split('\n') if linea]

        for i, line in enumerate(validation):
            self.assertEqual(line, test_data[i])

if __name__ == '__main__':
    unittest.main()
