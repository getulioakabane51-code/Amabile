import pytest
from app.maturity import maturity_level


def test_maturity_level():
    average, level, name = maturity_level({
        "strategy": 3,
        "people": 2,
        "processes": 3,
        "data": 2,
        "governance": 2,
    })
    assert average == 2.4
    assert level == 2
    assert name == "Operacional"


def test_invalid_score():
    with pytest.raises(ValueError):
        maturity_level({
            "strategy": 6,
            "people": 2,
            "processes": 3,
            "data": 2,
            "governance": 2,
        })
