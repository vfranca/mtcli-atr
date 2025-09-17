import pytest
from mtcli_atr.atr import calcular_atr


def gerar_rates_simples(qtd, high=110, low=100, close=105):
    """Gera candles falsos com valores constantes."""
    return [{"high": high, "low": low, "close": close} for _ in range(qtd)]


def test_calcula_atr_com_dados_suficientes():
    periodo = 3
    rates = [
        {"high": 110, "low": 100, "close": 105},
        {"high": 115, "low": 105, "close": 110},
        {"high": 120, "low": 110, "close": 115},
        {"high": 125, "low": 115, "close": 120},
    ]
    atr = calcular_atr(rates, periodo)
    # TRs esperados: 15, 15, 15 => ATR = 15
    assert pytest.approx(atr, 0.01) == 10


def test_erro_se_dados_insuficientes():
    periodo = 5
    rates = gerar_rates_simples(3)
    with pytest.raises(ValueError, match="Quantidade insuficiente de dados"):
        calcular_atr(rates, periodo)


def test_calculo_com_valores_variados():
    periodo = 2
    rates = [
        {"high": 110, "low": 100, "close": 105},
        {"high": 120, "low": 100, "close": 110},  # TR = max(20, 15, 10) = 20
        {"high": 125, "low": 110, "close": 120},  # TR = max(15, 15, 10) = 15
    ]
    atr = calcular_atr(rates, periodo)
    assert pytest.approx(atr, 0.01) == 17.5
