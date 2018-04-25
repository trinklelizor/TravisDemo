import unittest
import time

class SimpleTests(unittest.TestCase):

    def test_should_succeed(self):
        assert 7 == 7
        
    def test_old_print_syntax(self):
        print ("Works in both")
        
if __name__ == "__main__":
    unittest.main()
