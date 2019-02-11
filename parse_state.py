class ParseState():

    _FAILURE = None

    @staticmethod
    def create_failure_state():
        failure = ParseState(None, None)
        failure._success = False
        return failure

    def __init__(self, node, remainder):
        self._success = True
        self._node = node
        self._remainder = remainder

        # Create FAILURE state if it doesn't already exist
        if ParseState._FAILURE is None:
            ParseState._FAILURE = ParseState.create_failure_state()

    def success(self):
        return self._success

    def node(self):
        return self._node

    def remainder(self):
        return self._remainder

    def has_no_remainder(self):
        return len(self._remainder) == 0