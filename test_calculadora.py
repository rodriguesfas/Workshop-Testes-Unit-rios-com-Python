import unittest
from calculadora import somar, eh_par

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)

    def test_eh_par(self):
        self.assertTrue(eh_par(4))
        self.assertFalse(eh_par(5))

if __name__ == '__main__':
    unittest.main()
