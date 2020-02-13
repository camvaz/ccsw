import unittest
from strats import Strats

class StratsTests(unittest.TestCase):
    def setUp(self):
        self.strat = Strats()
    
    def testCommaSeparatedValue(self):
        self.assertEqual(['Queen', '9', 'Metallica', '7', 'Doors', '8', 'Nirvana', '6'],
                         self.strat.prueba_1("Queen, 9, Metallica, 7, Doors, 8, Nirvana, 6"))

if __name__ == '__main__':
    unittest.main()