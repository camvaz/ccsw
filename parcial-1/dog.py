#=== TEST EXAMPLE WITH DOG CLASS
import unittest

class Dog:
    def __init__(self):
        self.name = "afea"

    def bark(self):
        return 'wof!'


class TestDog(unittest.TestCase):
    def setUp(self):
        self.dog = Dog()

    def test_upper(self):
        self.assertEqual('wof!', self.dog.bark())


if __name__ == '__main__':
    unittest.main()