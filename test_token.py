import pytest
from tokenclass import Token

def test_token_is_abstract():
    with pytest.raises(TypeError):
        Token()