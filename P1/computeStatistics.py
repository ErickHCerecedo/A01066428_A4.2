import sys
import time

class ComputeStatistics:
    def __init__(self, input_file):
        self.input_file = input_file

    # Función para calcular la media
    def calculate_mean(self, data):
        return sum(data) / len(data)

    # Función para calcular la mediana
    def calculate_median(self, data):
        sorted_data = sorted(data)
        length_data = len(data)

        if length_data % 2 == 0:
            median = (sorted_data[length_data // 2 - 1] + sorted_data[length_data // 2]) / 2
        else:
            median = sorted_data[length_data // 2]
        return median

    # Funcion para calcular la moda
    def calculate_mode(self, data):
        count_dict = {}
        for item in data:
            count_dict[item] = count_dict.get(item, 0) + 1
        mode = [key for key, value in count_dict.items() if value == max(count_dict.values())]
        return mode

    # Función para calcular la desviación estándar
    def calculate_standard_deviation(self, data, mean):
        squared_diff = [(x - mean) ** 2 for x in data]
        variance = sum(squared_diff) / len(data)
        return variance ** 0.5

    # Función principal
    def calculate_statistics(self):
        try:
            with open(self.input_file, 'r') as file:
                data = []
                for line in file:
                    try:
                        value = float(line.strip())
                        data.append(value)
                    except ValueError:
                        print(f"Invalid data: {line.strip()}")
                        continue

            start_time = time.time()

            count = len(data)
            mean = self.calculate_mean(data)
            median = self.calculate_median(data)
            mode = self.calculate_mode(data)
            standard_deviation = self.calculate_standard_deviation(data, mean)
            variance = standard_deviation ** 2

            end_time = time.time()
            elapsed_time = end_time - start_time

            with open("StatisticsResults.txt", 'w') as result_file:
                result_file.write(f"COUNT:    {count}\n")
                result_file.write(f"MEAN:     {mean}\n")
                result_file.write(f"MEDIAN:   {median}\n")
                result_file.write(f"MODE:     {mode}\n")
                result_file.write(f"SD:       {standard_deviation}\n")
                result_file.write(f"VARIANCE: {variance}\n")
                result_file.write(f"Elapsed Time: {elapsed_time} seconds\n")

            print(f"COUNT:    {count}")
            print(f"MEAN:     {mean}")
            print(f"MEDIAN:   {median}")
            print(f"MODE:     {mode}")
            print(f"SD:       {standard_deviation}")
            print(f"VARIANCE: {variance}")
            print(f"Elapsed Time: {elapsed_time} seconds")

        except FileNotFoundError:
            print(f"File '{self.input_file}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <input_file>")
    else:
        input_file = sys.argv[1]
        calculator = ComputeStatistics(input_file)
        calculator.calculate_statistics()