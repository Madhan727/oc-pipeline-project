
from app import add, get_status


def test_add():
    assert add(2, 3) == 5


def test_get_status():
    assert get_status() == "SERVICERUNNING"
