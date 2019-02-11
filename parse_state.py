import copy

class ParseState():

    # Static FAILURE state
    _FAILURE = None

    # Build a new ParseState with the given 'node' and 'remainder' arguments
    @staticmethod
    def build(node, remainder):
        if node is None:
            raise ValueError('ParseStates need a \'node\' argument')
        elif remainder is None:
            raise ValueError('ParseStates need a \'remainder\' argument')
        
        return ParseState(node, copy.deepcopy(remainder))

    # Init takes arguments for current processed tree and remaining Token list
    def __init__(self, node, remainder):
        self._success = True
        self._node = node
        self._remainder = remainder

    # Getter for self._success
    def success(self):
        return self._success

    # Getter for self._node
    def node(self):
        return self._node

    # Getter for self._remainder
    def remainder(self):
        return copy.deepcopy(self._remainder)

    # Check whether there is no remainder. Returns True if remainder list is empty
    def has_no_remainder(self):
        return len(self._remainder) == 0

# TA: Is there a better way to do this? I couldn't get the _FAILURE static
# variable assigned any other way (not cleanly at least).
# Creates the _FAILURE static ParseState member of ParseState
def _create_failure_state():
    # Block any duplicate runs
    if ParseState._FAILURE is not None:
        return

    ParseState._FAILURE = ParseState(None, None)
    ParseState._FAILURE._success = False

# Create the _FAILURE state on module load
_create_failure_state()