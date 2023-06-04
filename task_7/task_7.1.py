import unittest
import random


def mult(a, b):

    c = a * b
    return c


a = random.randint(1, 10)
b = random.randint(1, 10)


def new(arr):
    for i in range(random.randint(1, 10)):
        arr.append(random.randint(1, 10))
    arr.append(5)
    return(arr)


arr = []


def convert(array_1):
    return (array_1)


array_1 = []
for j in range(5):
    array_1.append(random.randint(1, 10))


class TestMethods(unittest.TestCase):

    def test_new(self):
        self.assertIn(7, new(arr))
        self.assertNotIn(-8, new(arr))

    def test_mult(self):
        self.assertTrue(mult(a, b) > a)
        self.assertFalse(mult(a, b) < a)

    def test_equal(self):
        self.assertCountEqual(array_1, convert(array_1))

    def test_less(self):
        self.assertLess(mult(a, b), a)

    def test_greater(self):
        self.assertGreater(a, mult(a, b))


if __name__ == '__main__':
    unittest.main()

