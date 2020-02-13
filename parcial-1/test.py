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

    def testSameNumbers(self):
        self.assertFalse(self.strat.prueba_7('Queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5'))

    def testDataFormat(self):
        self.assertFalse(self.strat.prueba_6('10, 0.1, 9, 0.3, 7, 0.4'))
    
    def testAlphanumericValues(self):
        self.assertFalse(self.strat.prueba_9('A$AP ROCKY, 10, $ign, 9'))

    def testNumsBetween1And10(self):
        self.assertFalse(self.strat.prueba_10('Queen, 11, Metallica, 18, Doors, -8, Nirvana, -7, Guns and Roses, 6, Caifanes, 5'))

    def testNumsNotNegative(self):
        self.assertFalse(self.strat.prueba_11('Queen, 11, Metallica, 18, Doors, -8, Nirvana, -7, Guns and Roses, 6, Caifanes, 5'))

    def testNumsinValues(self):
        self.assertEqual(0, self.strat.prueba_12('Queen, Metallica, Doors, Nirvana, Guns and Roses'))

    def testStringsInValues(self):
        self.assertEqual(6, self.strat.prueba_13('Queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5'))

    def testStringsLessThan50Chars(self):
        self.assertTrue(self.strat.prueba_14('Queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5'))

    def testStringsMoreThan50Chars(self):
        self.assertTrue(self.strat.prueba_15('Queeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeen, 10'))
    
    def testNoFloatingNumbers(self):
        self.assertFalse(self.strat.prueba_16('Queen, 10.1, Metallica, 8, Doors, 8, Nirvana, 7.9, Guns and Roses, 6.1, Caifanes, 5.2'))
    
    def testNoRepeatedStrings(self):
        self.assertFalse(self.strat.prueba_17('Queen, 10, Queen, 10, Queen, 10, Queen, 10, Queen, 10'))
    
    def testStringsStartWithUpper(self):
        self.assertFalse(self.strat.prueba_18('queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5'))

    def testNumberAsDigit(self):
        self.assertFalse(self.strat.prueba_19('Queen, ten, Metallica, 9, Doors, eight'))

    def testNumbersCorrectSize(self):
        self.assertTrue(self.strat.prueba_20('Queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5'))
        
if __name__ == '__main__':
    unittest.main()
    