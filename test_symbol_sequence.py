import pytest
from symbol_sequence import SymbolSequence
from symbol_sequence import _create_epsilon_state
from connector import Connector
from variable import Variable
from terminal_symbol import TerminalSymbol
from parse_state import ParseState

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

# Helper method to generate a SymbolSequence with an empty production
def _generate_empty_symbol_sequence():
    return [], SymbolSequence.EPSILON

# Helper method to generate a SymbolSequence with one Token in it
def _generate_1_token_symbol_sequence():
    production = [Connector.build(TerminalSymbol.OPEN)]
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

# Match should raise ValueError when token_list is None
def test_match_error_on_none_token_list():
    _, seq = _generate_test_symbol_sequence()

    with pytest.raises(ValueError):
        seq.match(None)

# Match should return a ParseState
def test_match_returns_parse_state():
    state = SymbolSequence.EPSILON.match([])

    assert type(state) is ParseState

# Test match empty seq with empty prod
def test_match_empty_seq_empty_prod():
    state = SymbolSequence.EPSILON.match([])

    assert state.success()
    assert state.remainder() == []

# Test match empty seq with 1 token prod
def test_match_empty_seq_1_token_prod():
    prod, _ = _generate_1_token_symbol_sequence()
    state = SymbolSequence.EPSILON.match(prod)

    assert state.success()
    assert state.remainder() == prod

# Test match empty seq with large prod
def test_match_empty_seq_large_prod():
    prod, _ = _generate_test_symbol_sequence()
    state = SymbolSequence.EPSILON.match(prod)

    assert state.success()
    assert state.remainder() == prod

# Test match 1 token seq with empty prod
def test_match_1_token_seq_empty_prod_fails():
    _, seq = _generate_1_token_symbol_sequence()
    prod, _ = _generate_empty_symbol_sequence()
    state = seq.match(prod)

    assert state is ParseState.FAILURE

# Test match 1 token seq with 1 token prod which matches
def test_match_1_token_seq_1_token_prod_matches():
    # Duplicate calls to construct a different prod reference than was used to make seq
    _, seq = _generate_1_token_symbol_sequence()
    prod, _ = _generate_1_token_symbol_sequence()
    state = seq.match(prod)

    assert state.success()
    assert state.remainder() == []

# Test match 1 token seq with 1 token prod which does not match
def test_match_1_token_seq__1_token_prod_fails():
    _, seq = _generate_1_token_symbol_sequence()
    prod = [Connector.build(TerminalSymbol.MINUS)]
    state = seq.match(prod)

    assert state is ParseState.FAILURE

# Test match 1 token seq with large prod which matches
def test_match_1_token_seq_large_prod_matches():
    seq = SymbolSequence.build([Connector.OPEN])
    prod, _ = _generate_test_symbol_sequence()
    state = seq.match(prod)

    assert state.success()
    assert state.remainder() == prod[1:]

# Test match 1 token seq with large prod which does not match
def test_match_1_token_seq_large_prod_fails():
    seq = SymbolSequence.build([Connector.CLOSE])
    prod, _ = _generate_test_symbol_sequence()
    state = seq.match(prod)

    assert state is ParseState.FAILURE

# Test match large seq with empty prod
def test_match_large_seq_empty_prod_fails():
    _, seq = _generate_test_symbol_sequence()
    prod = []
    state = seq.match(prod)

    assert state is ParseState.FAILURE

# Test match large seq with 1 token prod
def test_match_large_seq_1_token_prod_fails():
    _, seq = _generate_test_symbol_sequence()
    prod, _ = _generate_1_token_symbol_sequence()
    state = seq.match(prod)

    assert state is ParseState.FAILURE

# Test match large seq with large prod which matches
def test_match_large_seq_large_prod_matches():
    # Duplicate calls to construct a different prod reference than was used to make seq
    _, seq = _generate_test_symbol_sequence()
    prod, _ = _generate_test_symbol_sequence()
    state = seq.match(prod)

    assert state.success()
    assert state.remainder() == []

# Test match large seq with large prod which does not match
def test_match_large_seq_large_prod_fails():
    _, seq = _generate_test_symbol_sequence()
    prod, _ = _generate_test_symbol_sequence()
    prod.insert(0, Variable.build('c'))
    state = seq.match(prod)

    assert state is ParseState.FAILURE