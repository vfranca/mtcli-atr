import pytest
from click.testing import CliRunner
from mtcli_atr.plugin import atr


def gerar_rates_fake(periodo):
    """Gera dados simulados para candles."""
    rates = []
    for i in range(periodo + 1):
        rates.append({"high": 110 + i, "low": 100 + i, "close": 105 + i})
    return rates


def test_atr_saida_valida(monkeypatch):
    periodo = 14
    symbol = "TESTE"
    timeframe = "D1"

    # Mock MetaTrader5
    monkeypatch.setattr("mtcli_atr.plugin.mt5.symbol_select", lambda s, v: True)
    monkeypatch.setattr(
        "mtcli_atr.plugin.mt5.copy_rates_from_pos",
        lambda *a, **kw: gerar_rates_fake(periodo),
    )
    monkeypatch.setattr("mtcli_atr.plugin.conectar", lambda: None)
    monkeypatch.setattr("mtcli_atr.plugin.shutdown", lambda: None)

    runner = CliRunner()
    result = runner.invoke(
        atr, ["--symbol", symbol, "--periodo", str(periodo), "--timeframe", timeframe]
    )

    assert result.exit_code == 0
    assert f"ATR({periodo}) de {symbol}" in result.output


def test_timeframe_invalido(monkeypatch):
    runner = CliRunner()
    result = runner.invoke(atr, ["--symbol", "TESTE", "--timeframe", "XX"])

    assert result.exit_code == 0
    assert "Timeframe inválido" in result.output


def test_symbol_nao_encontrado(monkeypatch):
    monkeypatch.setattr("mtcli_atr.plugin.mt5.symbol_select", lambda s, v: False)
    monkeypatch.setattr("mtcli_atr.plugin.conectar", lambda: None)
    monkeypatch.setattr("mtcli_atr.plugin.shutdown", lambda: None)

    runner = CliRunner()
    result = runner.invoke(atr, ["--symbol", "XXXX"])

    assert result.exit_code == 0
    assert "Erro ao selecionar símbolo" in result.output


def test_dados_insuficientes(monkeypatch):
    periodo = 14
    monkeypatch.setattr("mtcli_atr.plugin.mt5.symbol_select", lambda s, v: True)
    monkeypatch.setattr(
        "mtcli_atr.plugin.mt5.copy_rates_from_pos",
        lambda *a, **kw: [{"high": 110, "low": 100, "close": 105}] * 5,
    )
    monkeypatch.setattr("mtcli_atr.plugin.conectar", lambda: None)
    monkeypatch.setattr("mtcli_atr.plugin.shutdown", lambda: None)

    runner = CliRunner()
    result = runner.invoke(atr, ["--symbol", "TESTE", "--periodo", str(periodo)])

    assert result.exit_code == 0
    assert "Dados insuficientes para cálculo do ATR" in result.output
