from unittest.mock import patch
from mtcli_atr.views.atr_view import exibir_resultado_atr, exibir_erro


@patch("mtcli_atr.views.atr_view.click.echo")
def test_exibir_resultado_atr(mock_echo):
    exibir_resultado_atr("IBOV", 14, "D1", 4.5)
    mock_echo.assert_called_once()


@patch("mtcli_atr.views.atr_view.click.echo")
def test_exibir_erro(mock_echo):
    exibir_erro("Erro de teste")
    mock_echo.assert_called_once_with("Erro: Erro de teste")
