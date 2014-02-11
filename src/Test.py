from Engine import *
import unittest

suite1 = engineTestSuite

class AllTests(unittest.TestCase):
    
    def runTest(self):
        unittest.TextTestRunner(verbosity=2).run(suite1) 

if __name__ == '__main__':
    unittest.main()