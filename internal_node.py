'''
Internal node class represents an internal node on the expression tree.
'''

from node import Node
from token import Token

class InternalNode(Node):

    def __init__(self, children):
        self._children = children

    # Return the string representation of the stored token
    def __str__(self):
        return "[" + str(self._children[0]) + "," + str(self._children[1]) + "]"

    # This is an internal node, so it returns the concatenation of its children's lists
    def toList(self):
        return [self._children[0].toList(), self._children[1].toList()]