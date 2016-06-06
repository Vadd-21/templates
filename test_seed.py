import unittest
import file #replace file with the file needed

class Test_batch(unittest.TestCase):
    def setUp(self):
        self.Class = file.Class() #replace Class with the class name to be tested
        
    def test_something_success(self):
        self.assertEqual(1, self.Class.function(1,0)) #this example assumes the function adds a and b
        
    def test_raise_error(self):
        self.assertRaises(TypeError, self.Class.function, "a", "b") #this example assumes the function needs non strings
        
    