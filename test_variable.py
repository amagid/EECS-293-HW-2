import pytest
from variable import Variable
from terminal_symbol import TerminalSymbol

def test_error_on_no_representation():
    with pytest.raises(ValueError):
        Variable(None)

def test_variable_caching():
    var = Variable.build('x')
    assert Variable.build('x') is var

def test_variable_type_matches():
    assert Variable.build('x').matches(TerminalSymbol.VARIABLE)

def test_variable_str():
    assert str(Variable.build('x')) == 'x'

def test_variable_representation():
    assert Variable.build('x').representation() == 'x'