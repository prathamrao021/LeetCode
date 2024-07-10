# LRU cache using dictionary and array
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.last = []
        self.cache = dict()

    def get(self, key: int) -> int:
        # print(self.cache.keys())
        if self.cache.get(key) != None:
            self.last.remove(key)
            self.last.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            self.cache[key] = value
            self.last.remove(key)
            self.last.append(key)
        else:
            if len(self.cache) == self.capacity:
                last_used = self.last.pop(0)
                self.last.append(key)
                del self.cache[last_used]
                self.cache[key] = value
                #remove least_recently_used and add new one
            else:
                self.cache[key] = value
                self.last.append(key)
        return None

if __name__ == "__main__":
    lru = LRUCache(2)
    print(lru.put(1,0))
    print(lru.put(2,2))
    print(lru.get(1))
    print(lru.put(3,3))
    print(lru.get(2))
    print(lru.put(4,4))
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))