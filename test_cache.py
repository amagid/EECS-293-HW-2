import pytest
from cache import Cache

@pytest.fixture
def cache():
    return Cache()

def _create_abc123_string():
    return 'abc123'

def test_error_on_no_key_supplied(cache);
    with pytest.raises(ValueError):
        cache.get(None)

def test_error_on_no_constructor_supplied(cache);
    with pytest.raises(ValueError):
        cache.get('test', None)

def test_creates_new_instance(cache):
    test_string = cache.get('test', _create_abc123_string)
    assert test_string == 'abc123', 'Cache must create new object with provided constructor'

def test_retrieves_existing_instance(cache):
    test_string = cache.get('test', _create_abc123_string)
    assert test_string is cache.get('test', _create_abc123_string), 'Cache must return existing objects'