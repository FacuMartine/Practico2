# Práctico 4 — Pruebas automatizadas de seguridad

## Objetivo

Implementar pruebas automatizadas de regresión para verificar las vulnerabilidades de los cinco ejercicios del repositorio.

Se utilizan los mismos tests en ambas ramas:

- **main:** versión vulnerable, donde las pruebas de seguridad deben fallar.
- **Practico-2:** versión corregida, donde todas las pruebas deben pasar.

## Herramientas utilizadas

- Python, Pytest y Requests.
- Java 17, JUnit 5 y Maven.
- Docker y Docker Compose.

## Preparación

Desde la carpeta principal del repositorio, crear y activar el entorno virtual:

`python3 -m venv ../.venv`

`source ../.venv/bin/activate`

Instalar las dependencias:

`python -m pip install -r requirements-test.txt`

## Ejecución de las pruebas

**Ejercicio 1 — SQL Injection (unitarias)**

`cd Ejercicio1`

`python -m pytest test_sqli.py -v`

**Ejercicio 2 — XSS (unitarias)**

`cd Ejercicio2`

`python -m pytest test_xss.py -v`

**Ejercicio 3 — File Upload (integración)**

`cd Ejercicio3`

`sudo docker compose up --build -d`

`python -m pytest test_upload.py -v`

`sudo docker compose down`

**Ejercicio 4 — SSTI y RCE (integración)**

`cd Ejercicio4`

`sudo docker compose up --build -d`

Esperar a que la aplicación responda HTTP 200 en `http://localhost:8080/`.

`python -m pytest test_ssti.py -v`

`sudo docker compose down`

**Ejercicio 5 — Insecure Storage (unitaria JUnit)**

`cd Ejercicio5`

`sudo docker run --rm -v "$PWD":/app -w /app maven:3.9.11-eclipse-temurin-17 mvn -Dtest=EncryptionServiceTest test`

Cada ejercicio se ejecuta desde su carpeta correspondiente. Los ejercicios 3 y 4 utilizan el mismo puerto, por lo que no deben levantarse simultáneamente.

## Resultados esperados

| Ejercicio | main | Practico-2 |
|---|---|---|
| 1 — SQLi | 2 FAILED | 2 PASSED |
| 2 — XSS | 1 FAILED, 1 PASSED | 2 PASSED |
| 3 — File Upload | 1 FAILED | 1 PASSED |
| 4 — SSTI y RCE | 2 FAILED | 2 PASSED |
| 5 — Insecure Storage | 1 FAILED | 1 PASSED |

En la rama main se esperan **7 pruebas de seguridad fallidas y 1 prueba funcional aprobada**.

En Practico-2 se esperan **8 pruebas aprobadas**.

Los fallos esperados deben corresponder a las aserciones de seguridad y no a errores de configuración o conexión.

## Conclusión

Las pruebas permiten comprobar automáticamente que las vulnerabilidades están presentes en la versión original y que las mitigaciones aplicadas en Practico-2 corrigen los comportamientos evaluados.