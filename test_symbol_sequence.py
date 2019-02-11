import pytest
from symbol_sequence import SymbolSequence
from symbol_sequence import _create_epsilon_state
from connector import Connector
from variable import Variable
from terminal_symbol import TerminalSymbol

# Helper method to generate a SymbolSequence for '(a+b)'
def _generate_test_symbol_sequence():
    production = [
        Connector.build(TerminalSymbol.OPEN),
        Variable.build('a'),
        Connector.build(TerminalSymbol.PLUS),
        Variable.build('b'),
        Connector.build(TerminalSymbol.CLOSE)
    ]
    return production, SymbolSequence.build(production)

# Test that SymbolSequence.EPSILON is created
def test_epsilon_is_correct_type():
    epsilon = SymbolSequence.EPSILON
    assert type(epsilon) is SymbolSequence

# Test that SymbolSequence.EPSILON has empty production
def test_epsilon_has_correct_attributes():
    epsilon = SymbolSequence.EPSILON
    assert type(epsilon._production) is list
    assert len(epsilon._production) == 0

# Test that the EPSILON generator function only truly runs once
def test_create_epsilon_ignores_duplicate_runs():
    epsilon = SymbolSequence.EPSILON
    _create_epsilon_state()
    assert epsilon is SymbolSequence.EPSILON

# Ensure that build() gives ValueError when production is None
def test_build_error_on_none_production():
    with pytest.raises(ValueError):
        SymbolSequence.build(None)

# Ensure that str(SymbolSequence) returns the same as str(SymbolSequence._production)
def test_str_delegates_to_production():
    production, seq = _generate_test_symbol_sequence()
    assert str(seq) == str(production)

# Ensure that the build_symbols() method assigns the production the same as build()
def test_build_symbols_assigns_production():
    production, seq = _generate_test_symbol_sequence()
    seq2 = SymbolSequence.build_symbols(production[0], production[1], production[2], production[3], production[4])

    assert seq._production == seq2._production

