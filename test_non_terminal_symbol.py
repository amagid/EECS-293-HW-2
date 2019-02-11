import pytest
from non_terminal_symbol import NonTerminalSymbol
from non_terminal_symbol import _create_expression_symbol, _create_expression_tail_symbol, _create_factor_symbol, _create_term_symbol, _create_term_tail_symbol, _create_unary_symbol
from non_terminal_symbol import _populate_expression_table, _populate_expression_tail_table, _populate_factor_table, _populate_term_table, _populate_term_tail_table, _populate_unary_table
from symbol_sequence import SymbolSequence

# List of NonTerminalSymbol names, symbol generator, and production_table populator functions
# Used in parametrization of static NonTerminalSymbol tests
NON_TERMINAL_SYMBOL_TYPES = [
        ('EXPRESSION', _create_expression_symbol, _populate_expression_table),
        ('EXPRESSION_TAIL', _create_expression_tail_symbol, _populate_expression_tail_table),
        ('TERM', _create_term_symbol, _populate_term_table),
        ('TERM_TAIL', _create_term_tail_symbol, _populate_term_tail_table),
        ('UNARY', _create_unary_symbol, _populate_unary_table),
        ('FACTOR', _create_factor_symbol, _populate_factor_table)
]

# Helper method to get a static NonTerminalSymbol by name
# Used primarily to smoothen parametrization
def _name_to_nts(name):
    return getattr(NonTerminalSymbol, name)

# Parametrize test to generate matching tests for all NonTerminalSymbols
@pytest.mark.parametrize(
    'nts_type', NON_TERMINAL_SYMBOL_TYPES
)
# Make sure NonTerminalSymbols are generated to correct type
def test_nts_is_correct_type(nts_type):
    # Get NonTerminalSymbol from name to ensure latest reference
    nts = _name_to_nts(nts_type[0])

    assert type(nts) is NonTerminalSymbol

# Parametrize test to generate matching tests for all NonTerminalSymbols
@pytest.mark.parametrize(
    'nts_type', NON_TERMINAL_SYMBOL_TYPES
)
# Make sure the attributes of NonTerminalSymbols are correct to specs
def test_nts_has_correct_attributes(nts_type):
    # Get NonTerminalSymbol from name to ensure latest reference
    nts = _name_to_nts(nts_type[0])

    assert type(nts._production_table) is list
    assert len(nts._production_table) > 0
    for production in nts._production_table:
        assert type(production) is SymbolSequence

# Parametrize test to generate matching tests for all NonTerminalSymbols
@pytest.mark.parametrize(
    'nts_type', NON_TERMINAL_SYMBOL_TYPES
)
# Ensure that the _create_expression_symbol method will not create duplicate instances
def test_create_methods_ignore_duplicate_runs(nts_type):
    # Get NonTerminalSymbol from name to ensure latest reference
    nts = _name_to_nts(nts_type[0])

    # Run static symbol generator for this type
    nts_type[1]()
    
    # Get NonTerminalSymbol again from name to ensure latest reference
    nts_updated = _name_to_nts(nts_type[0])

    assert nts is nts_updated

# Parametrize test to generate matching tests for all NonTerminalSymbols
@pytest.mark.parametrize(
    'nts_type', NON_TERMINAL_SYMBOL_TYPES
)
# Ensure that the _populate_expression_table method will not populate multiple times
def test_populate_expression_table_ignores_duplicate_runs(nts_type):
    # Get NonTerminalSymbol's _production_table from name to ensure latest reference
    nts_prod = _name_to_nts(nts_type[0])._production_table

    # Run production_table populator for this type
    nts_type[2]()
    
    # Get NonTerminalSymbol's _production_table again from name to ensure latest reference
    nts_prod_updated = _name_to_nts(nts_type[0])._production_table

    assert nts_prod is nts_prod_updated