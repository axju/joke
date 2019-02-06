import unittest
from joke.facts import *

class TestFacts(unittest.TestCase):

    def test_cat(self):
        fact = cat()
        self.assertTrue(len(fact)>0)

if __name__ == '__main__':
    unittest.main()
