'''
Internal node class represents an internal node on the expression tree.
'''
import copy
from node import Node
from tokenclass import Token

class InternalNode(Node):

    # Builder nested class
    class Builder():
        def __init__(self):
            self._children = []

        # Remove childless nodes and collapse single-child nodes
        def simplify(self):
            pass

        # Convert to InternalNode
        def build(self):
            return InternalNode.build(self._children)

        # Add a child to this Builder
        def add_child(self, node):
            self._children.append(node)
            return True


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

    # Return a copy of this node's children
    def get_children(self):
        return copy.copy(self._children)

    # Return True if this node has children
    def is_fruitful(self):
        return len(self._children) > 0