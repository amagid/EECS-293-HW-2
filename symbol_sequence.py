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
