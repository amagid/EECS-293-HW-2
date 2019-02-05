'''
Variable class represents an Abstract Token which is specifically a variable.
'''
from token import TerminalSymbol
from abstract_token import AbstractToken
from cache import Cache

class Variable(AbstractToken):

    # Static cache to prevent creation of duplicate variables
    _cache = Cache()

    # Static method to build and return a new Variable with the given name (representation)
    @staticmethod
    def build(representation):
        return Variable._cache.get(representation, Variable)

    def __init__(self, representation):

        # Guard against initialization without a representation argument
        if representation is None:
            raise ValueError("New Variables must have a Representation argument")

        # Assign internal _type and _representation fields
        self._type = TerminalSymbol.VARIABLE
        self._representation = representation

    # Override __str__ to return this Variable's name (representation)
    def __str__(self):
        return self._representation

    # Get and return the name of this Variable
    def representation(self):
        return self._representation