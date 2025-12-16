import unittest
import requests

class TestTransferencias(unittest.TestCase):

    BASE_URL = "http://localhost:8000/api/transferencias"

    def test_transferencia_exitosa(self):
        payload = {
            "monto": 10000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("transferencia_exitosa", response.json())

    def test_exceder_limite_diario(self):
        payload = {
            "monto": 60000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("limite_diario_excedido", response.json())

    def test_exceder_limite_mensual(self):
        payload = {
            "monto": 5100000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("limite_mensual_excedido", response.json())

    def test_saldo_insuficiente(self):
        payload = {
            "monto": 1000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("saldo_insuficiente", response.json())

    def test_token_otp_invalido(self):
        payload = {
            "monto": 1500000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321",
            "otp": "123456"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("otp_invalido", response.json())

    def test_horario_mantenimiento(self):
        payload = {
            "monto": 10000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 503)
        self.assertIn("horario_mantenimiento", response.json())

    def test_cuenta_destino_invalida(self):
        payload = {
            "monto": 10000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0000000000"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("cuenta_destino_invalida", response.json())

    def test_transferencia_monto_minimo(self):
        payload = {
            "monto": 0.01,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertIn(response.status_code, [200, 400])

    def test_transferencia_monto_negativo(self):
        payload = {
            "monto": -10000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("monto_invalido", response.json())

    def test_transferencia_decimales_excesivos(self):
        payload = {
            "monto": 10.123,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("formato_monto_invalido", response.json())

    def test_concurrencia_transferencias(self):
        payload = {
            "monto": 500,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response1 = requests.post(self.BASE_URL, json=payload)
        response2 = requests.post(self.BASE_URL, json=payload)
        self.assertIn(response1.status_code, [200, 400])
        self.assertIn(response2.status_code, [200, 400])

    def test_cuenta_bloqueada(self):
        payload = {
            "monto": 10000,
            "cuenta_origen": "1111111111",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("cuenta_bloqueada", response.json())

    def test_cuenta_origen_igual_destino(self):
        payload = {
            "monto": 10000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "1234567890"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("cuenta_origen_destino_iguales", response.json())

    def test_transferencia_limite_diario(self):
        payload = {
            "monto": 50000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("transferencia_exitosa", response.json())

    def test_transferencia_limite_mensual(self):
        payload = {
            "monto": 5000000,
            "cuenta_origen": "1234567890",
            "cuenta_destino": "0987654321"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("transferencia_exitosa", response.json())

if __name__ == "__main__":
    unittest.main()