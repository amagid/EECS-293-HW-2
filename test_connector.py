import pytest
from connector import Connector
from terminal_symbol import TerminalSymbol

def test_error_on_no_token_type():
    with pytest.raises(ValueError):
        Connector.build(None)
        
def test_error_on_variable_token_type():
    with pytest.raises(ValueError):
        Connector.build(TerminalSymbol.VARIABLE)

def test_connector_caching():
    conn = Connector.build(TerminalSymbol.PLUS)
    assert conn is Connector.build(TerminalSymbol.PLUS)

def test_connector_type_matches():
    conn = Connector.build(TerminalSymbol.MINUS)
    assert Connector.matches(conn, TerminalSymbol.MINUS)

def test_connector_str():
    assert str(Connector.build(TerminalSymbol.DIVIDE)) == '/'