from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()     # gives hashmap + linked list functionality

    def get(self, key: int) -> int:
        if key in self._cache:
            # used so move to tail (recently used)
            self._cache.move_to_end(key)
            return self._cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, update
        if key in self._cache:
            self._cache.move_to_end(key)
            self._cache[key] = value
        else:   # key doesn't exist 
            if len(self._cache) == self._capacity: # already full -> pop oldest (in front)
                self._cache.popitem(last=False)
            self._cache[key] = value    # auto appends to end



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)