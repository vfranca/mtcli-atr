import pytest

from mtcli_atr.models.atr_model import calcular_atr


def test_calcular_atr_valido():
    rates = [
        {"high": 110, "low": 100, "close": 105},
        {"high": 112, "low": 101, "close": 108},
        {"high": 114, "low": 103, "close": 109},
    ]
    resultado = calcular_atr(rates, 2)
    assert isinstance(resultado, float)
    assert resultado > 0


def test_calcular_atr_dados_insuficientes():
    rates = [{"high": 110, "low": 100, "close": 105}]
    with pytest.raises(ValueError):
        calcular_atr(rates, 2)
