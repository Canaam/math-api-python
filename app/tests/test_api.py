# -*- coding: utf-8 -*-

import unittest
import json
from app.app import app  # Importa a aplicação Flask para testes

class TestAPI(unittest.TestCase):
    """Testes para os endpoints da API."""

    def setUp(self):
        """Configuracao inicial para cada teste."""
        self.app = app.test_client()
        self.app.testing = True

    def test_sum_valid_numbers(self):
        """Testa a soma de uma lista de numeros valida."""
        payload = {"numbers": [1, 2, 3, 4, 5]}
        response = self.app.post('/sum', data=json.dumps(payload), content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 15})

    def test_sum_invalid_input(self):
        """Testa a soma com entrada invalida (numeros misturados com strings)."""
        payload = {"numbers": [1, "a", 3]}
        response = self.app.post('/sum', data=json.dumps(payload), content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)

    def test_average_valid_numbers(self):
        """Testa a media de uma lista valida de numeros."""
        payload = {"numbers": [1, 2, 3, 4, 5]}
        response = self.app.post('/average', data=json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 3.0})

    def test_average_empty_list(self):
        """Testa a media quando a lista esta vazia."""
        payload = {"numbers": []}
        response = self.app.post('/average', data=json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)

    def test_average_invalid_input(self):
        """Testa a media com entrada invalida (strings no array)."""
        payload = {"numbers": ["x", 2, 3]}
        response = self.app.post('/average', data=json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)

if __name__ == '__main__':
    unittest.main()