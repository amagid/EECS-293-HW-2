'''
Abstract Token class extends and fully implements the Token base class.
'''

from token import Token, TerminalSymbol

class AbstractToken(Token):

    # Internal type storage
    _type = None

    # Init assigns this AbstractToken's type
    def __init__(self, token_type):
        self._type = token_type

    # Retrieve and return this Token's type
    def get_type(self):
        return self._type

    # Check whether this Token matches the supplied type, and return the result
    def matches(self, token_type):
        return token_type == self._type