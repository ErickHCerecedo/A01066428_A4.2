#pylint: disable=invalid-name
"""
convertNumbers.py

Este modulo ...
"""
import sys
import time

class ConvertNumbers:
    """
    A class for converting numbers from a file to binary and hexadecimal base.

    Args:
        input_file (str): The name of the input file containing numbers.
        output_file (str): The name of the output file to save the conversion results.
    """

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.generated_data = ""

    def convert_to_binary(self, number):
        """
        Convert a decimal number to binary and hexadecimal bases.

        Args:
            number (int): The decimal number to be converted.

        Returns:
            tuple: A tuple containing the binary and hexadecimal representations.
        """
        if number == 0:
            return '0'

        binary = ''

        if number < 0:
            number = number & 0x3FF

        while number > 0:
            remainder = number % 2
            binary = str(remainder) + binary
            number //= 2

        return binary

    def convert_to_hexadecimal(self, number):
        """
        Convert a decimal number to binary and hexadecimal bases.

        Args:
            number (int): The decimal number to be converted.

        Returns:
            tuple: A tuple containing the binary and hexadecimal representations.
        """
        if number == 0:
            return '0'

        hex_characters = '0123456789ABCDEF'
        hexadecimal = ''

        if number < 0:
            number = number & 0xFFFFFFFFFF

        while number > 0:
            remainder = number % 16
            hexadecimal = hex_characters[remainder] + hexadecimal
            number //= 16

        return hexadecimal

    def process_file(self):
        """
        Process the input file, converting numbers and writing results to the output file.
        """
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f_input, \
                 open(self.output_file, 'a', encoding='utf-8') as f_output:
                start_time = time.time()

                # Agrega la primera línea con encabezados
                first_line = "NUMBER\tTC\tBIN\tHEX\n"
                f_output.write(first_line)
                print(first_line, end='')

                number = 0
                for line in f_input:
                    try:
                        tc = int(line.strip())
                        binary = self.convert_to_binary(tc)
                        hexadecimal = self.convert_to_hexadecimal(tc)
                        number += 1
                        # Formatea la línea de resultados
                        result_line = f"{number}\t{tc}\t{binary}\t{hexadecimal}\n"
                    except ValueError:
                        error = "#VALUE!"
                        number += 1
                        result_line = f"{number}\t{line.strip()}\t{error}\t{error}\n"

                    # Imprime y escribe la línea de resultados
                    print(result_line, end='')
                    self.generated_data += result_line
                    f_output.write(result_line)

                end_time = time.time()
                elapsed_time = end_time - start_time

                # Imprime y escribe el tiempo de ejecución
                execution_time = f"Execution time: {elapsed_time:.2f} seconds\n\n\n"
                print(execution_time, end='')
                f_output.write(execution_time)
        except FileNotFoundError:
            print(f"File not found: {self.input_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
    else:
        given_file = sys.argv[1]
        result_file = "ConvertionResults.txt"
        converter = ConvertNumbers(given_file, result_file)
        converter.process_file()
