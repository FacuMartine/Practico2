
from unittest.mock import Mock, patch
import app


def test_sqli():
    db = Mock()

    with patch.object(app, "get_db", return_value=db):
        app.buscar_funciones("' OR 1=1 --", "nombre", "ASC")

    sql = db.execute.call_args.args[0]

    assert "LIKE ?" in sql


def test_ordenamiento():
    db = Mock()

    with patch.object(app, "get_db", return_value=db):
        app.buscar_funciones("Matrix", "nombre", "DESC; DROP TABLE peliculas; --")

    sql = db.execute.call_args.args[0]

    assert sql.strip().endswith("ORDER BY peliculas.nombre ASC")
