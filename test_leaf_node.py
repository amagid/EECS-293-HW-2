import pytest
from leaf_node import LeafNode
from connector import Connector
from terminal_symbol import TerminalSymbol

def test_error_on_no_token():
    with pytest.raises(ValueError):
        LeafNode.build(None)

def test_str_with_connector():
    ln = LeafNode(Connector.build(TerminalSymbol.PLUS))
    assert str(ln) == '+'

def test_to_list_with_connector():
    conn = Connector.build(TerminalSymbol.PLUS)
    ln = LeafNode(conn)
    assert ln.to_list() == [conn]