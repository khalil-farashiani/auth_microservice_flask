import pytest

from authman.authman import db

def test_database(app):
    with app.app_context():
        result = db.engine.execute("SELECT database();").first()
    assert result[0] == "testing"
