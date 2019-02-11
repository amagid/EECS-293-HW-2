import pytest
from symbols import Symbol

# Ensure Symbol class cannot be instantiated
def test_symbol_is_abstract():
    with pytest.raises(TypeError):
        Symbol()