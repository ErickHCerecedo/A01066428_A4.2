#pylint: disable=invalid-name
"""
convertNumbers.py

Este modulo ...
"""
import time

class WordCounter:
    """
    A class for counting words from a file.

    Args:
        filename (str): The name of the input file contain data.
    """

    def __init__(self, filename):
        self.filename = filename

    def count_words(self):
        """
        Contador de palabras.

        Returns:
            word_count: Un entero con la cantidad de palabras.
        """
        start_time = time.time()
        word_count = {}
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    words = line.split()
                    for word in words:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
        except FileNotFoundError:
            print(f"Error al leer el archivo")
            return

        elapsed_time = time.time() - start_time
        self.print_results(word_count, elapsed_time)

    def print_results(self, word_count, elapsed_time):
        """
        Imprime y guarda el resultado de Contador de palabras.

        Args:
            word_count:     Contador de palabras
            elapsed_time:   Tiempo transcurrido
        """
        with open('WordCountResults.txt', 'w', encoding='utf-8') as file:
            for word, count in word_count.items():
                print(f"{word}: {count}")
                file.write(f"{word}: {count}\n")
            print(f"Tiempo transcurrido: {elapsed_time} segundos")
            #file.write(f"Tiempo transcurrido: {elapsed_time} segundos\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py <archivo>")
    else:
        counter = WordCounter(sys.argv[1])
        counter.count_words()
