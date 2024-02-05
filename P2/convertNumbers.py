"""
convertNumbers.py

Este modulo ...
"""
import sys
import time

class ConvertNumbers:

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert_to_binary_and_hexadecimal(self, number):
        # Convierte un número a binario y hexadecimal
        binary = bin(number)[2:]
        hexadecimal = hex(number)[2:]
        return binary, hexadecimal

    def process_file(self):
        try:
            with open(self.input_file, 'r') as f_input, open(self.output_file, 'w') as f_output:
                start_time = time.time()
                for line in f_input:
                    try:
                        number = int(line.strip())
                        binary, hexadecimal = self.convert_to_binary_and_hexadecimal(number)
                        print(f"Decimal: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}")
                        f_output.write(f"Decimal: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}\n")
                    except ValueError:
                        print(f"Invalid data in the file: {line.strip()}")
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Execution time: {elapsed_time:.2f} seconds")
                f_output.write(f"Execution time: {elapsed_time:.2f} seconds\n")
        except FileNotFoundError:
            print(f"File not found: {self.input_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
    else:
        input_file = sys.argv[1]
        output_file = "ConvertionResults.txt"
        converter = NumberConverter(input_file, output_file)
        converter.process_file()
