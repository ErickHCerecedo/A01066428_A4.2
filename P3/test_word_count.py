"""
test_word_count.py

Clase para implementar casos de prueba para la clase wordCount.py
"""
import unittest
import re
from wordCount import WordCounter


class TestWordCounter(unittest.TestCase):
    """Clase para los casos de prueba"""

    def setUp(self):
        self.test_cases = [
            'TC1.txt',
            'TC2.txt',
            'TC3.txt',
            'TC4.txt',
            'TC5.txt'
        ]
        self.validation_files = [
            'TC1.Results.txt',
            'TC2.Results.txt',
            'TC3.Results.txt',
            'TC4.Results.txt',
            'TC5.Results.txt'
        ]

    def create_word_map(self, file):
        word_map = {}
        for line in file:
            words = line.split()
            for word in words:
                if re.match("^[A-Za-z]*$", word):
                    if word in word_map:
                        word_map[word] += 1
                    else:
                        word_map[word] = 1
        return word_map

    def test_tc1(self):
        """Caso de prueba 1"""
        counter = WordCounter(self.test_cases[0])
        counter.count_words()

        with open('WordCountResults.txt', 'r', encoding='utf-8') as result_file, \
             open(self.validation_files[0], 'r', encoding='utf-8') as validation_file:
            
            result_data = self.create_word_map(result_file)
            validation_data = self.create_word_map(validation_file)
            
            for word, result_freq in result_data.items():
                validation_freq = validation_data.get(word, 0)
                if result_freq != validation_freq:
                    print(word)
                self.assertEqual(result_freq, validation_freq)

    def test_tc2(self):
        """Caso de prueba 2"""
        counter = WordCounter(self.test_cases[1])
        counter.count_words()

        with open('WordCountResults.txt', 'r', encoding='utf-8') as result_file, \
             open(self.validation_files[1], 'r', encoding='utf-8') as validation_file:
            
            result_data = self.create_word_map(result_file)
            validation_data = self.create_word_map(validation_file)
            
            for word, result_freq in result_data.items():
                validation_freq = validation_data.get(word, 0)
                if result_freq != validation_freq:
                    print(word)
                self.assertEqual(result_freq, validation_freq)
    
    def test_tc3(self):
        """Caso de prueba 3"""
        counter = WordCounter(self.test_cases[2])
        counter.count_words()

        with open('WordCountResults.txt', 'r', encoding='utf-8') as result_file, \
             open(self.validation_files[2], 'r', encoding='utf-8') as validation_file:
            
            result_data = self.create_word_map(result_file)
            validation_data = self.create_word_map(validation_file)
            
            for word, result_freq in result_data.items():
                validation_freq = validation_data.get(word, 0)
                if result_freq != validation_freq:
                    print(word)
                self.assertEqual(result_freq, validation_freq)

    def test_tc4(self):
        """Caso de prueba 4"""
        counter = WordCounter(self.test_cases[3])
        counter.count_words()

        with open('WordCountResults.txt', 'r', encoding='utf-8') as result_file, \
             open(self.validation_files[3], 'r', encoding='utf-8') as validation_file:
            
            result_data = self.create_word_map(result_file)
            validation_data = self.create_word_map(validation_file)
            
            for word, result_freq in result_data.items():
                validation_freq = validation_data.get(word, 0)
                if result_freq != validation_freq:
                    print(word)
                self.assertEqual(result_freq, validation_freq)

    def test_tc5(self):
        """Caso de prueba 5"""
        counter = WordCounter(self.test_cases[4])
        counter.count_words()

        with open('WordCountResults.txt', 'r', encoding='utf-8') as result_file, \
             open(self.validation_files[4], 'r', encoding='utf-8') as validation_file:
            
            result_data = self.create_word_map(result_file)
            validation_data = self.create_word_map(validation_file)
            
            for word, result_freq in result_data.items():
                validation_freq = validation_data.get(word, 0)
                if result_freq != validation_freq:
                    print(word)
                self.assertEqual(result_freq, validation_freq)

if __name__ == '__main__':
    unittest.main()
