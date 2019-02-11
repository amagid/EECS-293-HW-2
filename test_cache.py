import pytest
from cache import Cache

def _create_cache():
    return Cache()

def _create_abc123_string(key_to_ignore):
    return 'abc123'

def test_error_on_no_key_supplied():
    _cache = _create_cache()
    with pytest.raises(ValueError):
        _cache.get(None, None)

def test_error_on_no_constructor_supplied():
    _cache = _create_cache()
    with pytest.raises(ValueError):
        _cache.get('test', None)

def test_creates_new_instance():
    _cache = _create_cache()
    test_string = _cache.get('test', _create_abc123_string)
    assert test_string == 'abc123'

def test_retrieves_existing_instance():
    _cache = _create_cache()
    test_string = _cache.get('test', _create_abc123_string)
    assert test_string is _cache.get('test', _create_abc123_string)