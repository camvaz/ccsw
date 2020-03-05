import unittest
from stats import Stats

class StatsTests(unittest.TestCase):
    def setUp(self):
        self.statsA = Stats([160,591,114,229,230,270,128,1657,624,1503])
        self.statsB = Stats([186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601])
        self.statsC = Stats([15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2])
    
    # Prueba 1 
    def testASet(self):
        self.assertEqual(self.statsA.standardDeviation(),572.03)

    # Prueba 2
    def testBSet(self):
        self.assertEqual(self.statsB.standardDeviation(),625.63)

    # Prueba 3
    def testCSet(self):
        self.assertEqual(self.statsC.standardDeviation(),62.26)

    # Prueba de promedio 
    def testavg(self):
        self.assertEqual(Stats([1,2,3]).mean(),2)

if __name__ == '__main__':
    unittest.main()