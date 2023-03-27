import unittest

def my_surname(surname):
    if surname.lower() == 'zlaya':
        return True
    else:
        return False

def even_digits(digits):
    a = []
    for digit in digits:
        if digit % 2 == 0:
            a.append(digit)
    return a

def words_len(word_1, word_2):
    return abs(len(word_1) - len(word_2))

def split_word(word):
    return list(word)

class TestFuncs(unittest.TestCase):
    def test_surname(self):
        self.assertTrue(my_surname('Zlaya'))
        self.assertFalse(my_surname('Ivanov'))
    def test_digit(self):
        some_digits = [1, 2, 8, 3]
        result = even_digits(some_digits)
        self.assertIn(2, result)
        self.assertNotIn(3, result)

    def test_words(self):
        greater_word = 'O wow what a long woooord'
        less_word = 'sml wrd'
        dif = words_len(greater_word, less_word)
        self.assertGreater(dif, len(less_word))
        self.assertLess(dif, len(greater_word))

    def test_count(self):
        word = 'apple'
        result = split_word(word)
        self.assertCountEqual(result, ['a', 'p', 'p', 'l', 'e'])


