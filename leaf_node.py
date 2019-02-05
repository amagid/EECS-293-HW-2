'''
Leaf node class represents a leaf node on the expression tree.
'''

from node import Node
from token import Token

class LeafNode(Node):

    @staticmethod
    def build(token):
        # Guard against missing token argument
        if token is None:
            raise ValueError("Leaf Nodes require a valid Token argument")

        return LeafNode(token)

    def __init__(self, token):
        self._token = token

    # Return the string representation of the stored token
    def __str__(self):
        return str(self._token)

    # This is a leaf node, so toList returns just this node's token in a Collection
    def toList(self):
        return [self.token]