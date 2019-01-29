'''
Variable class represents an Abstract Token which is specifically a variable.
'''
from token import TerminalSymbol
from abstract_token import AbstractToken
from cache import Cache

class Connector(AbstractToken):

    _cache = Cache()

    # Static method to build and return a new Variable with the given name (representation)
    @staticmethod
    def build(token_type):
        return Connector._cache.get(token_type, Connector)

    def __init__(self, token_type):

        # Guard against initialization without a representation argument
        if token_type == None:
            raise ValueError("New Connectors must have a token_type argument")
        elif token_type == TerminalSymbol.VARIABLE:
            raise ValueError("New Connectors cannot be of Variable type")

        # Assign internal _type field
        self._type = token_type

    # Override __str__ to return this Variable's name (representation)
    def __str__(self):
        if self._type == TerminalSymbol.PLUS:
            return "+"
        elif self._type == TerminalSymbol.MINUS:
            return "-"
        elif self._type == TerminalSymbol.TIMES:
            return "*"
        elif self._type == TerminalSymbol.DIVIDE:
            return '/'
        elif self._type == TerminalSymbol.OPEN:
            return '('
        elif self._type == TerminalSymbol.CLOSE:
            return ')'
        else:
            raise ValueError("Invalid Type")