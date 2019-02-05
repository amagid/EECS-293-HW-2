'''
TerminalSymbol enum provides encoding for different types of Tokens
'''

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