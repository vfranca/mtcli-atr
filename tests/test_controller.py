from unittest.mock import patch

import pytest

from mtcli_atr.controllers.atr_controller import processar_atr


@patch("mtcli_atr.controllers.atr_controller.mt5")
@patch("mtcli_atr.controllers.atr_controller.calcular_atr")
def test_processar_atr_valido(mock_calc, mock_mt5):
    mock_mt5.TIMEFRAME_D1 = "D1"
    mock_mt5.symbol_select.return_value = True
    mock_mt5.copy_rates_from_pos.return_value = [
        {"high": 110, "low": 100, "close": 105}
    ] * 15
    mock_calc.return_value = 5.0

    valor = processar_atr("IBOV", 14, "D1")
    assert valor == 5.0


@patch("mtcli_atr.controllers.atr_controller.mt5")
def test_processar_atr_timeframe_invalido(mock_mt5):
    mock_mt5.TIMEFRAME_D1 = "D1"
    with pytest.raises(ValueError):
        processar_atr("IBOV", 14, "ZZ")


@patch("mtcli_atr.controllers.atr_controller.mt5")
def test_processar_atr_symbol_select_falha(mock_mt5):
    mock_mt5.TIMEFRAME_D1 = "D1"
    mock_mt5.symbol_select.return_value = False
    with pytest.raises(RuntimeError):
        processar_atr("IBOV", 14, "D1")


@patch("mtcli_atr.controllers.atr_controller.mt5")
def test_processar_atr_dados_insuficientes(mock_mt5):
    mock_mt5.TIMEFRAME_D1 = "D1"
    mock_mt5.symbol_select.return_value = True
    mock_mt5.copy_rates_from_pos.return_value = []
    with pytest.raises(RuntimeError):
        processar_atr("IBOV", 14, "D1")
