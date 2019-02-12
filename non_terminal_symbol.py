from symbols import Symbol
from terminal_symbol import TerminalSymbol
from symbol_sequence import SymbolSequence
from parse_state import ParseState

class NonTerminalSymbol(Symbol):
    EXPRESSION = None
    EXPRESSION_TAIL = None
    TERM = None
    TERM_TAIL = None
    UNARY = None
    FACTOR = None
    PRODUCTIONS = None

    # Attempt to parse token_list as an EXPRESSION. Return None if fails
    @staticmethod
    def parse_input(token_list):
        # Attempt to parse the token_list as an EXPRESSION
        state = NonTerminalSymbol.EXPRESSION.parse(token_list)
        
        # If the parse was successful and has no remainder (fully parsed), return the resulting node
        if state.success() and state.has_no_remainder():
            return state.node()

        # If parse failed (or didn't fully complete), return None
        return None

    def __init__(self):
        self._production_table = []

    # Parse the token_list as this NonTerminalSymbol
    def parse(self, token_list):
        # Guard against None token_list
        if token_list is None:
            raise ValueError('NonTerminalSymbol cannot parse None token_list')

        # Check each SymbolSequence in the table, return first successful match
        state = None
        for symbol_seq in self._production_table:
            state = symbol_seq.match(token_list)

            # If the parse succeeded, return the resulting ParseState
            if state is not ParseState.FAILURE:
                return state
        
        # No matches found, so return FAILURE
        return ParseState.FAILURE


# TA: Is there a better way to do this? I couldn't get the static
# variables assigned any other way (not cleanly at least).

# Create all static NonTerminalSymbols

# Create EXPRESSION NTS
def _create_expression_symbol():
    # Block duplicate runs
    if NonTerminalSymbol.EXPRESSION is not None:
        return

    NonTerminalSymbol.EXPRESSION = NonTerminalSymbol()

# Create EXPRESSION_TAIL NTS
def _create_expression_tail_symbol():
    # Block duplicate runs
    if NonTerminalSymbol.EXPRESSION_TAIL is not None:
        return

    NonTerminalSymbol.EXPRESSION_TAIL = NonTerminalSymbol()

# Create TERM NTS
def _create_term_symbol():
    # Block duplicate runs
    if NonTerminalSymbol.TERM is not None:
        return

    NonTerminalSymbol.TERM = NonTerminalSymbol()

# Create TERM_TAIL NTS
def _create_term_tail_symbol():
    # Block duplicate runs
    if NonTerminalSymbol.TERM_TAIL is not None:
        return

    NonTerminalSymbol.TERM_TAIL = NonTerminalSymbol()

# Create UNARY NTS
def _create_unary_symbol():
    # Block duplicate runs
    if NonTerminalSymbol.UNARY is not None:
        return

    NonTerminalSymbol.UNARY = NonTerminalSymbol()

# Create FACTOR NTS
def _create_factor_symbol():
    # Block duplicate runs
    if NonTerminalSymbol.FACTOR is not None:
        return

    NonTerminalSymbol.FACTOR = NonTerminalSymbol()

# Populate _production_tables for all static NonTerminalSymbols

# Populate _production_table of EXPRESSION NTS
def _populate_expression_table():
    if NonTerminalSymbol.EXPRESSION._production_table != []:
        return

    NonTerminalSymbol.EXPRESSION._production_table = [
        SymbolSequence.build([
            NonTerminalSymbol.TERM,
            NonTerminalSymbol.EXPRESSION_TAIL
        ])
    ]

# Populate _production_table of EXPRESSION_TAIL NTS
def _populate_expression_tail_table():
    if NonTerminalSymbol.EXPRESSION_TAIL._production_table != []:
        return

    NonTerminalSymbol.EXPRESSION_TAIL._production_table = [
        SymbolSequence.build([
            TerminalSymbol.PLUS,
            NonTerminalSymbol.TERM,
            NonTerminalSymbol.EXPRESSION_TAIL
        ]),
        SymbolSequence.build([
            TerminalSymbol.MINUS,
            NonTerminalSymbol.TERM,
            NonTerminalSymbol.EXPRESSION_TAIL
        ]),
        SymbolSequence.EPSILON
    ]

# Populate _production_table of TERM NTS
def _populate_term_table():
    if NonTerminalSymbol.TERM._production_table != []:
        return

    NonTerminalSymbol.TERM._production_table = [
        SymbolSequence([
            NonTerminalSymbol.UNARY,
            NonTerminalSymbol.TERM_TAIL
        ])
    ]

# Populate _production_table of TERM_TAIL NTS
def _populate_term_tail_table():
    if NonTerminalSymbol.TERM_TAIL._production_table != []:
        return

    NonTerminalSymbol.TERM_TAIL._production_table = [
        SymbolSequence([
            TerminalSymbol.TIMES,
            NonTerminalSymbol.UNARY,
            NonTerminalSymbol.TERM_TAIL
        ]),
        SymbolSequence([
            TerminalSymbol.DIVIDE,
            NonTerminalSymbol.UNARY,
            NonTerminalSymbol.TERM_TAIL
        ]),
        SymbolSequence.EPSILON
    ]

# Populate _production_table of UNARY NTS
def _populate_unary_table():
    if NonTerminalSymbol.UNARY._production_table != []:
        return

    NonTerminalSymbol.UNARY._production_table = [
        SymbolSequence([
            TerminalSymbol.MINUS,
            NonTerminalSymbol.FACTOR
        ]),
        SymbolSequence([
            NonTerminalSymbol.FACTOR
        ])
    ]

# Populate _production_table of FACTOR NTS
def _populate_factor_table():
    if NonTerminalSymbol.FACTOR._production_table != []:
        return

    NonTerminalSymbol.FACTOR._production_table = [
        SymbolSequence([
            TerminalSymbol.OPEN,
            NonTerminalSymbol.EXPRESSION,
            TerminalSymbol.CLOSE
        ]),
        SymbolSequence([
            TerminalSymbol.VARIABLE
        ])
    ]    

# Create all static NonTerminalSymbols
def _create_static_symbols():
    _create_expression_symbol()
    _create_expression_tail_symbol()
    _create_term_symbol()
    _create_term_tail_symbol()
    _create_unary_symbol()
    _create_factor_symbol()

# Populate _production_tables for all static NonTerminalSymbols
def _populate_static_tables():
    _populate_expression_table()
    _populate_expression_tail_table()
    _populate_term_table()
    _populate_term_tail_table()
    _populate_unary_table()
    _populate_factor_table()

def _create_expression_map():
    sequences = NonTerminalSymbol.EXPRESSION._production_table
    return {
        TerminalSymbol.VARIABLE: sequences[0],
        TerminalSymbol.PLUS: None,
        TerminalSymbol.MINUS: sequences[0],
        TerminalSymbol.TIMES: None,
        TerminalSymbol.DIVIDE: None,
        TerminalSymbol.OPEN: sequences[0],
        TerminalSymbol.CLOSE: None,
        None: None
    }
    
def _create_expression_tail_map():
    sequences = NonTerminalSymbol.EXPRESSION_TAIL._production_table
    return {
        TerminalSymbol.VARIABLE: sequences[2],
        TerminalSymbol.PLUS: sequences[0],
        TerminalSymbol.MINUS: sequences[1],
        TerminalSymbol.TIMES: sequences[2],
        TerminalSymbol.DIVIDE: sequences[2],
        TerminalSymbol.OPEN: sequences[2],
        TerminalSymbol.CLOSE: sequences[2],
        None: sequences[2]
    }
    
def _create_term_map():
    sequences = NonTerminalSymbol.TERM._production_table
    return {
        TerminalSymbol.VARIABLE: sequences[0],
        TerminalSymbol.PLUS: None,
        TerminalSymbol.MINUS: sequences[0],
        TerminalSymbol.TIMES: None,
        TerminalSymbol.DIVIDE: None,
        TerminalSymbol.OPEN: sequences[0],
        TerminalSymbol.CLOSE: None,
        None: None
    }
    
def _create_term_tail_map():
    sequences = NonTerminalSymbol.TERM_TAIL._production_table
    return {
        TerminalSymbol.VARIABLE: sequences[2],
        TerminalSymbol.PLUS: sequences[2],
        TerminalSymbol.MINUS: sequences[2],
        TerminalSymbol.TIMES: sequences[0],
        TerminalSymbol.DIVIDE: sequences[1],
        TerminalSymbol.OPEN: sequences[2],
        TerminalSymbol.CLOSE: sequences[2],
        None: sequences[2]
    }
    
def _create_unary_map():
    sequences = NonTerminalSymbol.UNARY._production_table
    return {
        TerminalSymbol.VARIABLE: sequences[1],
        TerminalSymbol.PLUS: None,
        TerminalSymbol.MINUS: sequences[0],
        TerminalSymbol.TIMES: None,
        TerminalSymbol.DIVIDE: None,
        TerminalSymbol.OPEN: sequences[1],
        TerminalSymbol.CLOSE: None,
        None: None
    }
    
def _create_factor_map():
    sequences = NonTerminalSymbol.FACTOR._production_table
    return {
        TerminalSymbol.VARIABLE: sequences[1],
        TerminalSymbol.PLUS: None,
        TerminalSymbol.MINUS: None,
        TerminalSymbol.TIMES: None,
        TerminalSymbol.DIVIDE: None,
        TerminalSymbol.OPEN: sequences[0],
        TerminalSymbol.CLOSE: None,
        None: None
    }

def _create_productions_map():
    NonTerminalSymbol.PRODUCTIONS = {
        NonTerminalSymbol.EXPRESSION: _create_expression_map(),
        NonTerminalSymbol.EXPRESSION_TAIL: _create_expression_tail_map(),
        NonTerminalSymbol.TERM: _create_term_map(),
        NonTerminalSymbol.TERM_TAIL: _create_term_tail_map(),
        NonTerminalSymbol.UNARY: _create_unary_map(),
        NonTerminalSymbol.FACTOR: _create_factor_map()
    }

# Create static and populate all static symbols on module load
_create_static_symbols()
_populate_static_tables()
_create_productions_map()