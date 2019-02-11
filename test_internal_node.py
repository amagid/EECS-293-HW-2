from internal_node import InternalNode

# Quick mock node class to allow for testing

class MockNode():
    def __init__(self):
        pass
    
    def to_list(self):
        return []

    def __str__(self):
        return '[]'

# Tests

def test_empty_children_str():
    node = InternalNode([])
    assert str(node) == '[]'

def test_empty_children_list():
    node = InternalNode([])
    assert node.to_list() == []

def test_recurse_on_1_child_str():
    node = InternalNode([1])
    assert str(node) == '[1]'

def test_recurse_on_1_child_list():
    node = InternalNode([MockNode()])
    assert node.to_list() == [[]]

def test_recurse_on_many_child_str():
    node = InternalNode([1,2,3])
    assert str(node) == '[1,2,3]'

def test_recurse_on_many_child_list():
    node = InternalNode([MockNode(), MockNode(), MockNode()])
    assert node.to_list() == [[], [], []]

