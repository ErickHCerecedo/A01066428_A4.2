#pylint: disable=invalid-name
"""
computeStatistics.py

Este módulo proporciona calcula estadísticas descriptivas a partir de un archivo de datos.
Las estadísticas calculadas incluyen media, mediana, moda, desviación estándar y varianza.
"""
import sys
import time


class ComputeStatistics:
    """
    Clase para calcular estadísticas descriptivas a partir de un archivo de datos.
    """

    def __init__(self, input_file):
        self.input_file = input_file
        self.statistics = {
            'count': 0,
            'count_total': 0,
            'mean': 0,
            'median': 0,
            'mode': [],
            'standard_deviation': 0,
            'variance': 0,
            'elapsed_time': 0
        }

    def count_data(self, data):
        """
        Cuenta la cantidad de datos válidos en una lista.

        Args:
            data (list): Una lista de datos.

        Returns:
            int: Cantidad de datos válidos.
        """
        count = 0
        for item in data:
            try:
                float(item)
                count += 1
            except ValueError:
                pass
        self.statistics['count'] = count

    def count_data_total(self, data):
        """
        Cuenta la cantidad de datos válidos en una lista.

        Args:
            data (list): Una lista de datos.

        Returns:
            int: Cantidad de datos válidos.
        """
        count = 0
        for item in data:
            count += 1
        self.statistics['count_total'] = count

    # Función para calcular la media
    def calculate_mean(self, data):
        """
        Calcula la media de una lista de datos numéricos.

        Args:
            data (list): Una lista de números.

        Returns:
            float: La media de los datos.
        """
        sum_data = 0
        for val in data:
            sum_data += val
        self.statistics['mean'] = sum_data / self.statistics['count']

    # Función para calcular la mediana
    def calculate_median(self, data):
        """
        Calcula la mediana de una lista de datos numéricos.

        Args:
            data (list): Una lista de números.

        Returns:
            float: La mediana de los datos.
        """
        sorted_data = sorted(data)
        if self.statistics['count'] % 2 == 0:
            median = (
                sorted_data[self.statistics['count'] // 2 - 1] +
                sorted_data[self.statistics['count'] // 2]) / 2
        else:
            median = sorted_data[self.statistics['count'] // 2]
        self.statistics['median'] = median

    # Función para calcular la moda
    def calculate_mode(self, data):
        """
        Calcula la moda de una lista de datos numéricos.

        Args:
            data (list): Una lista de números.

        Returns:
            list: Una lista de los valores modales (puede ser más de uno).
        """
        frequency_dict = {}
        for val in data:
            if val in frequency_dict:
                frequency_dict[val] += 1
            else:
                frequency_dict[val] = 1
        
        # Encuentra el valor o los valores con la frecuencia máxima
        mode = []
        max_frequency = 0  # Inicializa el valor máximo en 0
        for freq in frequency_dict.values():
            if freq > max_frequency:
                max_frequency = freq
        
        for val, freq in frequency_dict.items():
            if max_frequency > 1:
                if freq == max_frequency:
                    mode.append(val)
            else:
                mode = ['N/A']
        self.statistics['mode'] = mode

    # Función para calcular la desviación estándar
    def calculate_standard_deviation(self, data):
        """
        Calcula la desviación estándar de una lista de datos numéricos.

        Args:
            data (list): Una lista de números.
            mean (float): La media de los datos.

        Returns:
            float: La desviación estándar de los datos.
        """
        sum_squared_diff = 0
        for x in data:
            squared_diff = (x - self.statistics['mean']) ** 2
            sum_squared_diff += squared_diff
        variance = sum_squared_diff / (self.statistics['count'] - 1)
        self.statistics['standard_deviation'] = variance ** 0.5

    # Función para calcular la varainza
    def calculate_variance(self, data):
        """
        Calcula la desviación estándar de una lista de datos numéricos.

        Args:
            data (list): Una lista de números.
            mean (float): La media de los datos.

        Returns:
            float: La desviación estándar de los datos.
        """
        sum_squared_diff = 0
        for x in data:
            squared_diff = (x - self.statistics['mean']) ** 2
            sum_squared_diff += squared_diff
        variance = sum_squared_diff / (self.statistics['count'] - 1)
        self.statistics['variance'] = variance

    # Función principal
    def calculate_statistics(self):
        """
        Calcula todas las estadísticas descriptivas y guarda los resultados en un archivo.
        """
        try:
            with open(self.input_file, 'r', encoding='utf-8') as file:
                data = []
                for line in file:
                    # Separa los valores por comas o punto y coma si están presentes
                    values = line.strip().split()#.replace(',', ' ').replace(';', ' ').split()
                    data.extend(values)

            start_time = time.time()

            self.count_data_total(data)
            # Filtra y convierte los valores válidos a números
            numeric_data = []
            for item in data:
                item = item.strip()
                try:
                    value = float(item)
                    numeric_data.append(value)
                except ValueError:
                    continue
            
            self.count_data(numeric_data)
            self.calculate_mean(numeric_data)
            self.calculate_median(numeric_data)
            self.calculate_mode(numeric_data)
            self.calculate_standard_deviation(numeric_data)
            self.calculate_variance(numeric_data)

            end_time = time.time()
            self.statistics['elapsed_time'] = end_time - start_time

            with open("StatisticsResults.txt", 'a', encoding='utf-8') as result_file:
                result_file.write(f"COUNT:    {self.statistics['count_total']}\n")
                result_file.write(f"MEAN:     {self.statistics['mean']}\n")
                result_file.write(f"MEDIAN:   {self.statistics['median']}\n")
                result_file.write(f"MODE:     {', '.join(map(str, self.statistics['mode']))}\n")
                result_file.write(f"SD:       {self.statistics['standard_deviation']}\n")
                result_file.write(f"VARIANCE: {self.statistics['variance']}\n")
                result_file.write(f"Elapsed Time: {self.statistics['elapsed_time']} seconds\n\n\n")

            print(f"COUNT:    {self.statistics['count_total']}")
            print(f"MEAN:     {self.statistics['mean']:.2f}")
            print(f"MEDIAN:   {self.statistics['median']:.2f}")
            print(f"MODE:     {', '.join(map(str, self.statistics['mode']))}")
            print(f"SD:       {self.statistics['standard_deviation']:.2f}")
            print(f"VARIANCE: {self.statistics['variance']:.2f}")
            print(f"Elapsed Time: {self.statistics['elapsed_time']} seconds\n\n")

        except FileNotFoundError:
            print(f"File '{self.input_file}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <input_file>")
    else:
        given_file = sys.argv[1]
        calculator = ComputeStatistics(given_file)
        calculator.calculate_statistics()
