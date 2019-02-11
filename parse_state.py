import copy

class ParseState():

    # Static FAILURE state
    _FAILURE = None

    # Generates the FAILURE ParseState
    @staticmethod
    def _create_failure_state():
        failure = ParseState(None, None)
        failure._success = False
        return failure

    # Build a new ParseState with the given 'node' and 'remainder' arguments
    @staticmethod
    def build(node, remainder)
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

        # Create FAILURE state if it doesn't already exist
        if ParseState._FAILURE is None:
            ParseState._FAILURE = ParseState._create_failure_state()

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