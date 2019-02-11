'''
Internal node class represents an internal node on the expression tree.
'''

from node import Node
from tokenclass import Token

class InternalNode(Node):

    # Static method to build and return a new InternalNode with the given children
    @staticmethod
    def build(children):
        # Guard against None children argument
        if children is None:
            raise ValueError('InternalNodes must receive an array of children')

        return InternalNode(children)

    def __init__(self, children):
        self._children = children

    # Return the string representation of the stored token
    def __str__(self):
        return '[' + ','.join(str(child) for child in self._children) + ']'

    # This is an internal node, so it returns the concatenation of its children's lists
    def to_list(self):
        output = []
        for child in self._children:
            output.append(child.to_list())

        return output