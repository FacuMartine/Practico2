
from flask import render_template
from app import app


def test_xss():
    pelicula = {
        "id": 1,
        "nombre": "Matrix",
        "genero": "Accion",
        "director": "Director",
        "descripcion": "<script>alert('XSS')</script>"
    }

    with app.app_context():
        html = render_template("edit.html", pelicula=pelicula)

    assert "<script>" not in html
    assert "&lt;script&gt;" in html


def test_descripcion_normal():
    pelicula = {
        "id": 1,
        "nombre": "Matrix",
        "genero": "Accion",
        "director": "Director",
        "descripcion": "Una pelicula de accion"
    }

    with app.app_context():
        html = render_template("edit.html", pelicula=pelicula)

    assert "Una pelicula de accion" in html
