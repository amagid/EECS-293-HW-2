'''
Main Token storage file, including general Token class and a makeshift
TerminalSymbol enum since as far as I'm aware, Python does not have enums.
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


class Token():

    # Blank init method since this class is not meant to be instantiated
    def __init__():
        pass

    # Retrieve and return this Token's type
    def get_type(self):
        pass

    # Check whether this Token matches the supplied type, and return the result
    def matches(self, token_type):
        pass