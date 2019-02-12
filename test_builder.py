import pytest
from internal_node import InternalNode
Builder = InternalNode.Builder
from test_non_terminal_symbol import _str_to_token_list
from non_terminal_symbol import NonTerminalSymbol

# Test add_child actually adds the child
# Test add_child returns True

# Test _post_process_node with no children returns None
# Test _post_process_node with one child returns that child simplified
# Test _post_process_node with a LeafNode returns the LeafNode
# Test _post_process_node with many children returns the given Node

# Test _collapse_none_children with no children returns empty list
# Test _collapse_none_children with one child returns list containing the child
# Test _collapse_none_children with many children and Nones returns only children in order

# Test build with no children returns empty InternalNode
# Test build with one LeafNode child returns the LeafNode
# Test build with one empty InternalNode child returns an empty InternalNode
# Test build with InternalNode that has one LeafNode child  returns the LeafNode
# Test build with InternalNode that has many LeafNode children returns an InternalNode with those children

# Test _simplify_node with a LeafNode returns the LeafNode
# Test _simplify_node with many children returns node with those children simplified

# Test simplify acts on all children
# Test simplify removes None children at end
# Test simplify does nothing when no children present
# Test simplify returns the given Builder

# Test build with no children returns empty InternalNode
# Test build with one LeafNode child returns the LeafNode
# Test build with one empty InternalNode child returns an empty InternalNode
# Test build with InternalNode that has one LeafNode child  returns the LeafNode
# Test build with InternalNode that has many LeafNode children returns an InternalNode with those children
# Test build on the assignment's given test expression, returns simplest possible string
def test_builder_simplify():
    SIMPLE_STRING = '[a,[+,[b,[/,c]]]]'
    node = NonTerminalSymbol.parse_input(_str_to_token_list('a+b/c'))
    b = InternalNode.Builder()
    b.add_child(node)
    b = b.build()

    assert str(b) == SIMPLE_STRING