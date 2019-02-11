import pytest
from non_terminal_symbol import NonTerminalSymbol
from non_terminal_symbol import _create_expression_symbol, _create_expression_tail_symbol, _create_factor_symbol, _create_term_symbol, _create_term_tail_symbol, _create_unary_symbol
from non_terminal_symbol import _populate_expression_table, _populate_expression_tail_table, _populate_factor_table, _populate_term_table, _populate_term_tail_table, _populate_unary_table
from symbol_sequence import SymbolSequence
from parse_state import ParseState
from variable import Variable
from connector import Connector
from terminal_symbol import TerminalSymbol

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

TERMINAL_SYMBOL_TRANSLATIONS = {
    '+': TerminalSymbol.PLUS,
    '-': TerminalSymbol.MINUS,
    '*': TerminalSymbol.TIMES,
    '/': TerminalSymbol.DIVIDE,
    '(': TerminalSymbol.OPEN,
    ')': TerminalSymbol.CLOSE
}

# Helper method to get a static NonTerminalSymbol by name
# Used primarily to smoothen parametrization
def _name_to_nts(name):
    return getattr(NonTerminalSymbol, name)

# Helper method to allow me to define tests more easily
# Takes a string expression representation and generates a token_list from it
def _str_to_token_list(expr):
    token_list = []
    for char in expr:
        if char in TERMINAL_SYMBOL_TRANSLATIONS:
            token_list.append(Connector.build(TERMINAL_SYMBOL_TRANSLATIONS[char]))
        else:
            token_list.append(Variable.build(char))
    return token_list

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

TEST_EXPRESSIONS = [
    (NonTerminalSymbol.FACTOR, '', False)
]

def _extract_from_test_expression(test_expr):
    return test_expr[0], _str_to_token_list(test_expr[1]), test_expr[2]

# Parametrize test to generate matching tests for all NonTerminalSymbols
@pytest.mark.parametrize(
    'test_expr', TEST_EXPRESSIONS
)
# Test various cases of specific NonTerminalSymbols attempting to parse expressions
def test_parse_by_sub_nts_types(test_expr):
    nts, expr, expected = _extract_from_test_expression(test_expr)
    state = nts.parse(expr)

    assert state.success() == expected

# Test FACTOR parse success (state only) of single-token list with a variable
# Test FACTOR parse success (state only) of 3-token list with a variable in parentheses
# Test FACTOR parse success (state only) of many-token list wrapped in parentheses
# Test FACTOR failure (state only) on many-token list not wrapped in parentheses

# Test UNARY failure (state only) on empty list
# Test UNARY parse success (state only) of single-token list with a variable
# Test UNARY parse success (state only) of two-token list with unary negation of a variable
# Test UNARY parse success (state only) of many-token list with an expression wrapped in parentheses
# Test UNARY parse success (state only) of many-token list with unary negation of expression wrapped in parentheses
# Test UNARY failure (state only) on term_tail two-token list [+, a]

# Test TERM_TAIL parse success (state only) of empty list
# Test TERM_TAIL parse success (state only) of two-token list with variable multiplication
# Test TERM_TAIL parse success (state only) of two-token list with variable division
# Test TERM_TAIL parse success (state only) of many-token list beginning with variable multiplication
# Test TERM_TAIL failure (state only) on many-token list beginning with not [*, /]

# Test TERM failure (state only) on empty list
# Test TERM parse success (state only) of single-token list with variable
# Test TERM parse success (state only) of three-token list with variable multiplication by variable
# Test TERM parse success (state only) of four-token list with unary negation in variable multiplication
# Test TERM failure (state only) on many-token list beginning with non-negation operator [+, *, /]

# Test EXPRESSION_TAIL parse success (state only) of empty list
# Test EXPRESSION_TAIL parse success (state only) of two-token list with variable addition
# Test EXPRESSION_TAIL parse success (state only) of two-token list with variable subtraction
# Test EXPRESSION_TAIL parse success (state only) of three-token list with double-negative variable
# Test EXPRESSION_TAIL parse success (state only) of many-token list with addition of complex sub-expression
# Test EXPRESSION_TAIL failure (state only) on single-token list with plus

# Test EXPRESSION error on None list
# Test EXPRESSION failure on empty list
# Test EXPRESSION parse of single-token list with variable
# Test EXPRESSION parse of two-token list with unary negation of variable
# Test EXPRESSION parse of many-token list with variable in parentheses
# Test EXPRESSION parse of many-token list with variable multiplication and then division in parentheses
# Test EXPRESSION parse of many-token list with variable addition and subtraction
# Test parse of assignment example input [a+b/c]
