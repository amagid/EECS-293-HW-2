'''
Variable class represents an Abstract Token which is specifically a variable.
'''
from token import TerminalSymbol
from abstract_token import AbstractToken

class Variable(AbstractToken):

    def __init__(self, representation):

        # Guard against initialization without a representation argument
        if representation == None:
            raise ValueError("New Variables must have a Representation argument")

        # Assign internal _type and _representation fields
        self._type = TerminalSymbol.VARIABLE
        self._representation = representation

    # Get and return the name of this variable
    def representation(self):
        return self._representation