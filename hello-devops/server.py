import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        """Configure the test client before each test"""
        self.app = app.test_client()
        self.app.testing = True  # Activer le mode test

    def test_home_route(self):
        """Test de la route '/'"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, CI/CD!")  # Vérifie le contenu de la réponse

    def test_status_route(self):
        """Test de la route '/status'"""
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "running")

if __name__ == "__main__":
    unittest.main()
