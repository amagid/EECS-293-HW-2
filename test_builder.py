import pytest
from internal_node import InternalNode
Builder = InternalNode.Builder
from test_non_terminal_symbol import _str_to_token_list
from non_terminal_symbol import NonTerminalSymbol
from leaf_node import LeafNode
from variable import Variable

# Test add_child actually adds the child
def test_add_child_adds_child():
    b = Builder()
    node = InternalNode.build([])
    b.add_child(node)

    assert b._children[0] is node

# Test add_child returns True
def test_add_child_returns_true():
    b = Builder()
    node = InternalNode.build([])
    result = b.add_child(node)

    assert result



# Test _post_process_node with no children returns None
def test_post_process_node_no_children():
    b = Builder()
    node = InternalNode.build([])

    assert b._post_process_node(node) is None

# Test _post_process_node with one child returns that child simplified
def test_post_process_node_one_child():
    b = Builder()
    deep_leaf_node = LeafNode.build(Variable.build('a'))
    node = InternalNode.build([InternalNode.build([deep_leaf_node])])

    assert b._post_process_node(node) is deep_leaf_node

# Test _post_process_node with many children returns the given Node
def test_post_process_node_many_children():
    b = Builder()
    node = InternalNode([
        LeafNode.build(Variable.build('a')),
        LeafNode.build(Variable.build('b')),
        LeafNode.build(Variable.build('c'))
    ])
    as_list = node.to_list()

    result = b._post_process_node(node)
    assert result is node
    assert result.to_list() == as_list



# Test _collapse_none_children with no children returns empty list
def test_collapse_none_children_no_children():
    b = Builder()
    output = b._collapse_none_children([])

    assert output == []

# Test _collapse_none_children with one child returns list containing the child
def test_collapse_none_children_one_child():
    b = Builder()
    output = b._collapse_none_children([1])

    assert output == [1]

# Test _collapse_none_children with many children and Nones returns only children in order
def test_collapse_none_children_many_children():
    b = Builder()
    output = b._collapse_none_children([None, 1, 2, None, None, 3, None, 4, None])

    assert output == [1,2,3,4]



# Test build with no children returns empty InternalNode
def test_build_no_children():
    b = Builder()
    result = b.build()

    assert type(result) is InternalNode
    assert result.get_children() == []

# Test build with one LeafNode child returns the LeafNode
def test_build_one_leaf_node_child():
    b = Builder()
    child = LeafNode.build(Variable.build('a'))
    b.add_child(child)
    result = b.build()

    assert result is child

# Test build with one empty InternalNode child returns an empty InternalNode
def test_build_one_empty_child():
    b = Builder()
    b.add_child(InternalNode.build([]))
    result = b.build()

    assert type(result) is InternalNode
    assert result.get_children() == []
    
# Test build with InternalNode that has one LeafNode child returns the LeafNode
def test_build_one_child_with_leaf_node_grandchild():
    b = Builder()
    grandchild = LeafNode.build(Variable.build('a'))
    child = InternalNode.build([grandchild])
    b.add_child(child)
    result = b.build()

    assert result is grandchild
    
# Test build with InternalNode that has many LeafNode children returns an InternalNode with those children
def test_build_many_leaf_node_children():
    b = Builder()
    children = [
        LeafNode.build(Variable.build('a')),
        LeafNode.build(Variable.build('b')),
        LeafNode.build(Variable.build('c'))
    ]
    b.add_child(InternalNode.build(children))
    result = b.build()

    assert type(result) is InternalNode
    assert len(result.get_children()) == len(children)
    for child in children:
        assert child in result.get_children()



# Test _simplify_node with a LeafNode returns the LeafNode
def test_simplify_node_with_leaf_node():
    b = Builder()
    child = LeafNode.build(Variable.build('a'))
    result = b._simplify_node(child)

    assert result is child

# Test _simplify_node with many children returns node with those children simplified
def test_simplify_node_with_many_children():
    b = Builder()
    grandchildren = [
        LeafNode.build(Variable.build('a')),
        LeafNode.build(Variable.build('b')),
        LeafNode.build(Variable.build('c'))
    ]
    for grandchild in grandchildren:
        b.add_child(InternalNode.build([grandchild]))

    result = b.build()

    assert type(result) is InternalNode
    assert len(result.get_children()) == len(grandchildren)
    for grandchild in grandchildren:
        assert grandchild in result.get_children()



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