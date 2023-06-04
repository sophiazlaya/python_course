import os
import unittest
import shutil

text = "hello my soulmate"


def func(path):
    os.makedirs(path, exist_ok=True)
    with open('new_file.txt', 'w') as f:
        f.write(text)


class Test(unittest.TestCase):

    def setUp(self):
        func('C:/Users/Sonya/python_course/new_folder')

    def testmethod(self):
        with open('new_file.txt', 'r') as f:
            self.assertFalse(os.stat('new_file.txt').st_size == 0)
            self.assertTrue(text == f.read())

    def tearDown(self):
        shutil.rmtree('C:/Users/Sonya/python_course/new_folder')


if __name__ == '__main__':
    unittest.main()