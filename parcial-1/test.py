import unittest
from strats import Strats

class StratsTests(unittest.TestCase):
    def setUp(self):
        self.strat = Strats()
        self.minValues = 5
        self.maxValues = 10

    def testCommaSeparatedValue(self):
        self.assertEqual(['Queen', '9', 'Metallica', '7', 'Doors', '8', 'Nirvana', '6'],
                         self.strat.prueba_1("Queen, 9, Metallica, 7, Doors, 8, Nirvana, 6"))

    def testLessThan5(self):
        self.assertFalse(self.strat.prueba_2('Queen, 9, Metallica, 7') >= self.minValues)
        
    def testLessThan10MoreThan5(self):
        self.assertTrue(self.strat.prueba_2('Queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5') <= self.maxValues and\
             self.strat.prueba_2('Queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5') >= self.minValues)
    
    def testLessThan10(self):
        self.assertFalse(self.strat.prueba_4('Queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5, '
                                            +'Molotov, 4, Kanye, 3, Tyler, 2, Rocky, 1, Joey, 0') <=10)
    
    def testOrderedNumbers(self):
        self.assertTrue(self.strat.prueba_5('Queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5'))

    def testDataInPlace(self):
        self.assertFalse(self.strat.prueba_6('10, Queen, 9, Metallica, 7, Nirvana'))

    


if __name__ == '__main__':
    unittest.main()
    