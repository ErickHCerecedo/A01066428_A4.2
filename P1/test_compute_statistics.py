#pylint: disable=line-too-long
"""
test_compute_statistic.py
"""
import unittest
from computeStatistics import ComputeStatistics

class TestComputeStatistics(unittest.TestCase):
    """Clase para los casos de prueba"""

    def load_data(self, filename):
        """Carga de datos"""
        with open(filename, 'r', encoding='utf-8') as file:
            data = [float(line.strip()) for line in file]
        return data

    # Prueba para TC1
    def test_tc1(self):
        """Caso de Prueba 1"""
        calculator = ComputeStatistics("TC1.txt")
        calculator.calculate_statistics()

        # Aserciones para verificar los resultados con los valores esperados
        self.assertEqual(calculator.statistics['count_total'], 400)
        self.assertAlmostEqual(calculator.statistics['mean'], 242.32, places=2)
        self.assertAlmostEqual(calculator.statistics['median'], 239.50, places=2)
        self.assertEqual(calculator.statistics['mode'], [393, 170])
        self.assertAlmostEqual(calculator.statistics['standard_deviation'], 145.4400206, places=7)
        self.assertAlmostEqual(calculator.statistics['variance'], 21152.7996, places=4)

    # Prueba para TC2
    def test_tc2(self):
        """Caso de Prueba 2"""
        calculator = ComputeStatistics("TC2.txt")
        calculator.calculate_statistics()

        # Aserciones para verificar los resultados con los valores esperados
        self.assertEqual(calculator.statistics['count_total'], 1977)
        self.assertAlmostEqual(calculator.statistics['mean'], 250.7840162, places=7)
        self.assertAlmostEqual(calculator.statistics['median'], 247.0000, places=4)
        self.assertEqual(calculator.statistics['mode'], [230])
        self.assertAlmostEqual(calculator.statistics['standard_deviation'], 144.2077, places=3)
        self.assertAlmostEqual(calculator.statistics['variance'], 20795.888043, places=3)

    # Prueba para TC3
    def test_tc3(self):
        """Caso de Prueba 3"""
        calculator = ComputeStatistics("TC3.txt")
        calculator.calculate_statistics()

        # Aserciones para verificar los resultados con los valores esperados
        self.assertEqual(calculator.statistics['count_total'], 12624)
        self.assertAlmostEqual(calculator.statistics['mean'], 249.7762, places=2)
        self.assertAlmostEqual(calculator.statistics['median'], 249.0000, places=2)
        self.assertEqual(calculator.statistics['mode'], [94])
        self.assertAlmostEqual(calculator.statistics['standard_deviation'], 145.3178498, places=1)
        self.assertAlmostEqual(calculator.statistics['variance'], 21118.95039, places=4)

    # Prueba para TC4
    def test_tc4(self):
        """Caso de Prueba 4"""
        calculator = ComputeStatistics("TC4.txt")
        calculator.calculate_statistics()

        # Aserciones para verificar los resultados con los valores esperados
        self.assertEqual(calculator.statistics['count_total'], 12624)
        self.assertAlmostEqual(calculator.statistics['mean'], 149.0026735, places=2)
        self.assertAlmostEqual(calculator.statistics['median'], 147.7500, places=2)
        self.assertEqual(calculator.statistics['mode'], [123.75])
        self.assertAlmostEqual(calculator.statistics['standard_deviation'], 130.4144196, places=1)
        self.assertAlmostEqual(calculator.statistics['variance'], 17009.26822, places=2)

    # Prueba para TC5
    def test_tc5(self):
        """Caso de Prueba 5"""
        calculator = ComputeStatistics("TC5.txt")
        calculator.calculate_statistics()

        # Aserciones para verificar los resultados con los valores esperados
        self.assertEqual(calculator.statistics['count_total'], 311)
        self.assertAlmostEqual(calculator.statistics['mean'], 241.50, places=2)
        self.assertAlmostEqual(calculator.statistics['median'], 241.00, places=2)
        self.assertEqual(calculator.statistics['mode'], [393.0, 19.0, 368.0, 290.0, 56.0, 11.0, 76.0, 215.0, 64.0, 375.0, 466.0, 277.0, 211.0, 46.0, 278.0, 170.0, 166.0, 96.0, 268.0])
        self.assertAlmostEqual(calculator.statistics['standard_deviation'], 145.7023416, places=2)
        self.assertAlmostEqual(calculator.statistics['variance'], 21229.17236, places=2)

    # Prueba para TC6
    def test_tc6(self):
        """Caso de Prueba 6"""
        calculator = ComputeStatistics("TC6.txt")
        calculator.calculate_statistics()

        # Aserciones para verificar los resultados con los valores esperados
        self.assertEqual(calculator.statistics['count_total'], 3000.00)
        self.assertAlmostEqual(calculator.statistics['mean'], 187906599279774728192.00, places=2)
        self.assertAlmostEqual(calculator.statistics['median'], 188008049965542998016.00, places=2)
        self.assertEqual(calculator.statistics['mode'], ['N/A'])
        self.assertAlmostEqual(calculator.statistics['standard_deviation'], 107399951657667608576.00, places=2)
        self.assertAlmostEqual(calculator.statistics['variance'], 11534749616069338239761958751339425038336.0, places=2)

    # Prueba para TC7
    def test_tc7(self):
        """Caso de Prueba 7"""
        calculator = ComputeStatistics("TC7.txt")
        calculator.calculate_statistics()

        # Aserciones para verificar los resultados con los valores esperados
        self.assertEqual(calculator.statistics['count_total'], 12769.00)
        self.assertAlmostEqual(calculator.statistics['mean'], 247467395499714904064.00, places=2)
        self.assertAlmostEqual(calculator.statistics['median'], 246640973074290016256.00, places=2)
        self.assertEqual(calculator.statistics['mode'], ['N/A'])
        self.assertAlmostEqual(calculator.statistics['standard_deviation'], 144611310601233121280.00, places=2)
        self.assertAlmostEqual(calculator.statistics['variance'], 20912431153806321107417444778947884613632.00, places=2)

if __name__ == "__main__":
    unittest.main()
