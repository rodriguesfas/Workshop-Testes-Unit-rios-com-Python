import unittest
from controllers import verificar_idade

class TestController(unittest.TestCase):

    def test_verificar_idade(self):
        self.assertEqual(verificar_idade(17), "Menor de idade")
        self.assertEqual(verificar_idade(18), "Maior de idade")

if __name__ == '__main__':
    unittest.main()
