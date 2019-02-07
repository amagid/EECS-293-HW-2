'''
Internal node class represents an internal node on the expression tree.
'''

from node import Node
from tokenclass import Token

class InternalNode(Node):

    def __init__(self, children):
        self._children = children

    # Return the string representation of the stored token
    def __str__(self):
        return '[' + ','.join(str(child) for child in self._children) + ']'

    # This is an internal node, so it returns the concatenation of its children's lists
    def toList(self):
        output = []
        for child in self._children:
            output.append(child.toList())

        return output