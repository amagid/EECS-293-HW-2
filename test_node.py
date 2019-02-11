import pytest
from node import Node

def test_node_is_abstract():
    with pytest.raises(TypeError):
        Node()