from hm11 import bubble_sort
import unittest

class Testbubble_sort(unittest.TestCase):
    def test_bubble_sort(self):
        list = [3, 1, 2]
        bubble_sort(list)
        self.assertEqual(list, [1, 2, 3])    
        
# нашел в гугле, не сам писал

print("smehpJERN")