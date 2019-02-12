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
            for child in self._children:
                self._simplify_node(child)

            return self

        def _simplify_node(self, node):
            children = node.get_children()

            # If this node is a leaf node, return the node
            if children is None:
                return node
            # If this node has no children, delete it
            elif len(children) == 0:
                return None
            # If this node has one child, replace this node with its child & recurse
            elif len(children) == 1:
                return self._simplify_node(children[0])

            # If this node has more than one child, recurse on children
            for i in range(0, len(children)):
                children[i] = self._simplify_node(children[i])

            # Remove children from list if they are None
            self._collapse_none_children(node)

            # Return the node so it can be added to the parent's _children list
            return node

        def _collapse_none_children(self, node):
            output = []
            for child in node.get_children():
                if child is not None:
                    output.append(child)

            node._children = output


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