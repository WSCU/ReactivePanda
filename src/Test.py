from Engine import *
import unittest

suite1 = engineTestSuite

class AllTests(unittest.TestCase):
    
    def runTest(self):
        suite1 

if __name__ == '__main__':
    unittest.main()