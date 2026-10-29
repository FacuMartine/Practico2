
import requests

def test_ssti():
    respuesta = requests.get(
        "http://localhost:8080/",
        params={"buscar": "1/0"},
        timeout=10
    )

    assert respuesta.status_code == 200
