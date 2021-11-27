import pytest

def test_env(app):
    assert app.config["ENV"] == "testing"
