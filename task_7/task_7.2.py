import unittest
import random



class TestRands(unittest.TestCase):

    def test_rands(self):
        n = 10
        numbers = []
        for x in range(n):
            numbers.append(random.random())

        for number in numbers:
            with self.subTest(rand=number):
                self.assertGreaterEqual(number, 0.5)


if __name__ == '__main__':
    unittest.main()