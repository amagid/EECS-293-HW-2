# Import unittest package
import unittest

# Import all testing files for this project
from test_abstract_token import TestAbstractToken
from test_cache import TestCache
from test_connector import TestConnector
from test_internal_node import TestInternalNode
from test_leaf_node import TestLeafNode
from test_node import TestNode
from test_terminal_symbol import TestTerminalSymbol
from test_token import TestToken
from test_variable import TestVariable

# Run the tests
if __name__ == '__main__':
    unittest.main()