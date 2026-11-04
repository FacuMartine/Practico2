
import requests

URL = "http://localhost:8080"


def test_ssti():
    respuesta = requests.get(
        URL,
        params={"buscar": "7*7"},
        timeout=10
    )

    assert respuesta.status_code == 200
    assert "Resultados buscando por: 49" not in respuesta.text
    assert "No se encontraron coincidencias." in respuesta.text


def test_rce():
    payload = "T(java.lang.Runtime).getRuntime().exec('printf DSS_PRUEBA')"

    respuesta = requests.get(
        URL,
        params={"buscar": payload},
        timeout=10
    )

    assert respuesta.status_code == 200
    assert "Process[pid=" not in respuesta.text
    assert "No se encontraron coincidencias." in respuesta.text
