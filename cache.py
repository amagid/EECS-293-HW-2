'''
Class to implement caching function. Exposes a 'get' method which retrieves
an object from the cache by key or creates a new object at the given key if no
such object currently exists.
'''
class Cache():
    _cache = {}

    def __init__(self):
        pass

    def get(self, key, constructor):
        try:
            return self._cache[key]
        except KeyError:
            if key == None:
                raise ValueError("No key passed")
            elif constructor == None:
                raise ValueError("Key not found, and no constructor passed to create new object")
            
            self._cache[key] = constructor()
    