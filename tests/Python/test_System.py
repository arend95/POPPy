import sys
import matplotlib.pyplot as pt
sys.path.append('../../')

import unittest
import numpy as np

import src.Python.Copy as Copy
import src.Python.System as System

class TestParabola(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        print("\nTesting System") 
        
    def setUp(self):
        lims_x = [-100, 100]
        lims_y = [-100, 100]
        gridsize = [101, 101]
        self.system = System.System()
        
    def test_setCustomBeamPath(self):
        test_path = '/this/is/the/path/to/test/'
        self.system.setCustomBeamPath(test_path)
        self.assertEqual(test_path, self.system.customBeamPath)
        
        to_append = 'and/the/test/goes/on/'
        self.system.setCustomBeamPath(to_append, append=True)
        self.assertEqual(test_path + to_append, self.system.customBeamPath)
        
    def test_addParabola(self):
        a = 100
        b = 100
        #### TODO: write tests
        
        
        
if __name__ == "__main__":
    unittest.main()
        
        
        
