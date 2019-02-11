'''
Connector class represents an Abstract Token which is specifically a Connector.
'''
from terminal_symbol import TerminalSymbol
from abstract_token import AbstractToken
from cache import Cache

SymbolTranslations = {
    TerminalSymbol.PLUS: '+',
    TerminalSymbol.MINUS: '-',
    TerminalSymbol.TIMES: '*',
    TerminalSymbol.DIVIDE: '/',
    TerminalSymbol.OPEN: '(',
    TerminalSymbol.CLOSE: ')'
}

class Connector(AbstractToken):

    _cache = Cache()

    # Static method to build and return a new Connector with the given type
    @staticmethod
    def build(token_type):
        return Connector._cache.get(token_type, Connector)

    def __init__(self, token_type):
        # Guard against initialization without a representation argument
        if token_type is None:
            raise ValueError("New Connectors must have a token_type argument")
            
        if token_type == TerminalSymbol.VARIABLE:
            raise ValueError("New Connectors cannot be of Variable type")

        # Assign internal _type field
        self._type = token_type

    # Override __str__ to return this Connector's type
    def __str__(self):
        if self._type in SymbolTranslations:
            return SymbolTranslations[self._type]
        else:
            raise ValueError("Invalid Symbol Type")

    def __eq__(self, obj):
        return type(obj) is Connector and str(obj) == str(self)

    def __ne__(self, obj):
        return not (self == obj)