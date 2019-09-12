import unittest
from joke.quotes import *

class TestQuotes(unittest.TestCase):

    def test_quotesondesign(self):
        quote = quotesondesign()
        self.assertTrue(quote)

        quotes = quotesondesign(5)
        self.assertEqual(len(quotes), 5)

        for quote in quotes:
            self.assertTrue(len(quote)>0)

        data = quotesondesign(format='data')
        self.assertIn('quote', data)
        self.assertIn('author', data)
        self.assertIn('id', data)

    def test_stormconsultancy(self):
        quote = stormconsultancy()
        self.assertTrue(len(quote)>0)

        data = stormconsultancy(5, format='data')
        self.assertEqual(data['id'], 5)
        self.assertIn('quote', data)
        self.assertIn('author', data)
        self.assertIn('id', data)

if __name__ == '__main__':
    unittest.main()
