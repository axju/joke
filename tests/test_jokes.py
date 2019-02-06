import unittest
from joke.jokes import *

class TestJokes(unittest.TestCase):

    def test_geek(self):
        joke = geek()
        self.assertTrue(len(joke)>0)

    def test_icanhazdad(self):
        joke = icanhazdad()
        self.assertTrue(len(joke)>0)

    def test_chucknorris(self):
        joke = chucknorris()
        self.assertTrue(len(joke)>0)

    def test_icndb(self):
        joke = icndb()
        self.assertTrue(len(joke)>0)

if __name__ == '__main__':
    unittest.main()
