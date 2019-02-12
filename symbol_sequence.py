from parse_state import ParseState
from internal_node import InternalNode

class SymbolSequence():

    EPSILON = None

    @staticmethod
    def build(production):
        if production is None:
            raise ValueError('SymbolSequences must have a \'production\' argument')

        return SymbolSequence(production)

    @staticmethod
    def build_symbols(*arg):
        return SymbolSequence(list(arg))

    def __init__(self, production):
        self._production = production

    def __str__(self):
        return str(self._production)

    def match(self, token_list):
        # Guard against None token_list
        if token_list is None:
            raise ValueError('SymbolSequence cannot match to None token_list')

        # Track remainder and children
        remainder = token_list
        builder = InternalNode.Builder()
        #children = []

        # Attempt to parse each Token in the list
        for prod_symbol in self._production:
            state = prod_symbol.parse(remainder)

            # Handle unsuccessful parse
            if not state.success():
                return ParseState.FAILURE

            # else add node to children and update remainder
            builder.add_child(state.node())
            remainder = state.remainder()
        
        # Return a ParseState containing a new InternalNode for the root and the remainder
        print(builder)
        print(builder._children)
        b = builder.build()
        print(b)
        return ParseState.build(b, remainder)

# TA: Is there a better way to do this? I couldn't get the EPSILON static
# variable assigned any other way (not cleanly at least).
# Creates the EPSILON static SymbolSequence member of SymbolSequence
def _create_epsilon_state():
    # Block any duplicate runs
    if SymbolSequence.EPSILON is not None:
        return

    SymbolSequence.EPSILON = SymbolSequence.build([])

# Create the EPSILON state on module load
_create_epsilon_state()
