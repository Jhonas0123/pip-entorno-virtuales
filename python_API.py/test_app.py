import unittest
from app import app

class SaludoApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_saludo_sin_parametro(self):
        response = self.client.get('/saludo')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'mensaje': 'Hola  desde la API de Python'})

    def test_saludo_con_parametro(self):
        response = self.client.get('/saludo?cadenadeentrada=Juan')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'mensaje': 'Hola Juan desde la API de Python'})

if __name__ == '__main__':
    unittest.main()