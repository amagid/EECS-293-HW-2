'''
TerminalSymbol enum provides encoding for different types of Tokens
'''
from symbols import Symbol
from leaf_node import LeafNode
from parse_state import ParseState

# TerminalSymbol enum
class TerminalSymbol(Symbol):
    VARIABLE = None
    PLUS = None
    MINUS = None
    TIMES = None
    DIVIDE = None
    OPEN = None
    CLOSE = None

    def __init__(self, terminal_type):
        self._type = terminal_type

    # Parse the first Token in the list and return a ParseState, return FAILURE state if fails
    def parse(self, token_list):
        if token_list[0].matches(self._type):
            return ParseState.build(LeafNode.build(token_list[0]), token_list[1:])
        else:
            return ParseState.FAILURE

# TA: Is there a better way to do this? I couldn't get the static
# variables assigned any other way (not cleanly at least).
# Create VARIABLE symbol
def _create_variable_symbol():
    # Block duplicate runs
    if TerminalSymbol.VARIABLE is not None:
        return

    TerminalSymbol.VARIABLE = TerminalSymbol(1)
    
# Create PLUS symbol
def _create_plus_symbol():
    # Block duplicate runs
    if TerminalSymbol.PLUS is not None:
        return

    TerminalSymbol.PLUS = TerminalSymbol(2)
    
# Create MINUS symbol
def _create_minus_symbol():
    # Block duplicate runs
    if TerminalSymbol.MINUS is not None:
        return

    TerminalSymbol.MINUS = TerminalSymbol(3)
    
# Create TIMES symbol
def _create_times_symbol():
    # Block duplicate runs
    if TerminalSymbol.TIMES is not None:
        return

    TerminalSymbol.TIMES = TerminalSymbol(4)
    
# Create DIVIDE symbol
def _create_divide_symbol():
    # Block duplicate runs
    if TerminalSymbol.DIVIDE is not None:
        return

    TerminalSymbol.DIVIDE = TerminalSymbol(5)
    
# Create OPEN symbol
def _create_open_symbol():
    # Block duplicate runs
    if TerminalSymbol.OPEN is not None:
        return

    TerminalSymbol.OPEN = TerminalSymbol(6)
    
# Create CLOSE symbol
def _create_close_symbol():
    # Block duplicate runs
    if TerminalSymbol.CLOSE is not None:
        return

    TerminalSymbol.CLOSE = TerminalSymbol(7)

# Create all static symbols
def _create_constant_symbols():
    _create_variable_symbol()
    _create_plus_symbol()
    _create_minus_symbol()
    _create_times_symbol()
    _create_divide_symbol()
    _create_open_symbol()
    _create_close_symbol()

# Create all static symbols on module load
_create_constant_symbols()