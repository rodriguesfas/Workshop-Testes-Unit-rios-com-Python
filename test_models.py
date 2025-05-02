import unittest
from models import User

class TestUser(unittest.TestCase):

    def test_criacao_user(self):
        user = User("João", "joao@email.com")
        self.assertEqual(user.name, "João")
        self.assertEqual(user.email, "joao@email.com")

    def test_saudacao(self):
        user = User("Ana", "ana@email.com")
        self.assertEqual(user.saudacao(), "Olá, Ana!")

if __name__ == '__main__':
    unittest.main()
