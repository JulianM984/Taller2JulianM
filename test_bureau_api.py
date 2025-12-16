import pytest
import requests

BASE_URL = "http://localhost:8000"

# Test data
TEST_DATA = [
    {"id": 1, "document": "123456789", "expected_status": 200, "expected_message": "Buen historial crediticio"},
    {"id": 2, "document": "987654321", "expected_status": 200, "expected_message": "Deudas activas"},
    {"id": 3, "document": "112233445", "expected_status": 200, "expected_message": "Cliente en lista de riesgo"},
    {"id": 4, "document": "000000000", "expected_status": 404, "expected_message": "Cliente no encontrado"},
    {"id": 5, "document": "ABC123456", "expected_status": 400, "expected_message": "Formato de documento inválido"},
    {"id": 6, "document": None, "expected_status": 503, "expected_message": "Servicio no disponible"},
    {"id": 7, "document": "123456789", "expected_status": 504, "expected_message": "Tiempo de espera agotado"},
    {"id": 8, "document": "123456789", "expected_status": 500, "expected_message": "Respuesta inválida del servicio"},
    {"id": 9, "document": "123123123", "expected_status": 409, "expected_message": "Documento duplicado"},
    {"id": 10, "document": "X12345678", "expected_status": 200, "expected_message": "Cliente extranjero, no aplica para consulta"},
    {"id": 11, "document": "456789123", "expected_status": 200, "expected_message": "Sin historial crediticio"},
    {"id": 12, "document": None, "expected_status": 400, "expected_message": "Documento requerido"},
    {"id": 13, "document": "@#$%^&*", "expected_status": 400, "expected_message": "Formato de documento inválido"},
    {"id": 14, "document": "654321987", "expected_status": 200, "expected_message": "Cliente fallecido, no aplica para consulta"},
    {"id": 15, "document": "789123456", "expected_status": 200, "expected_message": "Cliente menor de edad, no aplica para consulta"},
]

@pytest.mark.parametrize("test_case", TEST_DATA)
def test_bureau_api(test_case):
    """
    Test the Bureau API with various scenarios.
    """
    document = test_case["document"]
    expected_status = test_case["expected_status"]
    expected_message = test_case["expected_message"]

    # Prepare the request
    url = f"{BASE_URL}/consulta-bureau"
    payload = {"document": document} if document else {}

    # Send the request
    try:
        response = requests.post(url, json=payload, timeout=5)
        assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
        assert expected_message in response.text, f"Expected message '{expected_message}' not found in response"
    except requests.exceptions.Timeout:
        assert expected_status == 504, "Expected timeout error"
    except requests.exceptions.ConnectionError:
        assert expected_status == 503, "Expected service unavailable error"