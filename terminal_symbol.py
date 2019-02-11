'''
TerminalSymbol enum provides encoding for different types of Tokens
'''

from enum import Enum
from symbols import Symbol
from leaf_node import LeafNode
from parse_state import ParseState

# TerminalSymbol enum
class TerminalSymbol(Enum, Symbol):
    VARIABLE = 1
    PLUS = 2
    MINUS = 3
    TIMES = 4
    DIVIDE = 5
    OPEN = 6
    CLOSE = 7

    def __init__(self, terminal_type):
        self._type = terminal_type

    # Parse the first Token in the list and return a ParseState, return FAILURE state if fails
    def parse(self, token_list):
        if any(token_list[0].matches(terminal_type) for terminal_type in [
            TerminalSymbol.PLUS,
            TerminalSymbol.MINUS,
            TerminalSymbol.TIMES,
            TerminalSymbol.DIVIDE,
            TerminalSymbol.OPEN,
            TerminalSymbol.CLOSE,
            TerminalSymbol.VARIABLE
        ]):
            return ParseState.build(LeafNode.build(token_list[0]), token_list[1:])
        else:
            return ParseState.FAILURE
