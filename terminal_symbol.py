'''
TerminalSymbol enum provides encoding for different types of Tokens
'''
from leaf_node import LeafNode
from parse_state import ParseState, FAILURE
from enum import Enum

# TerminalSymbol enum
class TerminalSymbol(Enum):
    VARIABLE = 1
    PLUS = 2
    MINUS = 3
    TIMES = 4
    DIVIDE = 5
    OPEN = 6
    CLOSE = 7

    # Parse the first Token in the list and return a ParseState, return FAILURE state if fails
    def parse(self, token_list):
        # Guard against parsing empty expression
        if len(token_list) == 0:
            return FAILURE
            
        if token_list[0].matches(self):
            return ParseState.build(LeafNode.build(token_list[0]), token_list[1:])
        else:
            return FAILURE

    # Getter for internal _type field
    def get_type(self):
        return self.value