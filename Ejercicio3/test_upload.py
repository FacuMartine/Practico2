
import os
import uuid
import requests

URL = os.getenv("EJ3_URL", "http://localhost:8080")


def test_rechaza_archivo_txt():
    nombre = f"prueba_{uuid.uuid4().hex}.txt"

    # Comprobamos que la aplicación esté funcionando
    pagina = requests.get(f"{URL}/upload/1", timeout=10)
    assert pagina.status_code == 200

    # Intentamos subir un archivo TXT
    respuesta = requests.post(
        f"{URL}/upload/1",
        files={"afiche": (nombre, b"archivo de prueba", "text/plain")},
        allow_redirects=False,
        timeout=10
    )

    assert respuesta.status_code == 302

    # Comprobamos que el archivo NO se haya guardado
    archivo = requests.get(f"{URL}/uploads/{nombre}", timeout=10)

    assert archivo.status_code == 404
