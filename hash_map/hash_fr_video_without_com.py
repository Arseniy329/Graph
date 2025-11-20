from typing import Any


class HashMap:
    def __init__(self):
        self.size = 8
        self.map = [None] * self.size

    def _get_hash(self, key) -> int:
        return hash(key) % self.size

    def add(self, key, value) -> None:

        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            self.map[key_hash] = (key_hash, key, value)
        else:
            print('collision')
            new_hash = self._probe(key_hash)
            if new_hash is not None:
                self.map[new_hash] = (key_hash, key, value)
            else:
                self._resize()
                self.add(key, value)

    def _probe(self, start_index) -> int | None:
        for i in range(start_index + 1, self.size + start_index):
            index = i % self.size
            if self.map[index] is None:
                return index

    def get(self, key) -> Any | None:
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None and self.map[key_hash][0] == key:
            return self.map[key_hash][1]
        else:
            for i in range(key_hash + 1, self.size + key_hash):
                index = i % self.size
                if self.map[index] is not None and self.map[index][0] == key:
                    return self.map[index][1]
        return None

    def delete(self, key) -> bool:
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None and self.map[key_hash][0] == key:
            self.map[key_hash] = None
        else:
            for i in range(key_hash + 1, self.size + key_hash):
                index = i % self.size
                if self.map[index] is not None and self.map[index][0] == key:
                    self.map[index] = None
                    return True
        return False

    def _resize(self) -> None:
        old_map = self.map
        self.size *= 2
        self.map = [None] * self.size
        for item in old_map:
            if item is not None:
                _, key, value = item
                self.add(key, value)

    def __str__(self):
        result = ""
        for item in self.map:
            if item is not None:
                result += str(item) + "\n"
        return result


hash_map = HashMap()

hash_map.add("key1", "value1")
hash_map.add("key2", "value2")
hash_map.add("key3", "value3")

print(hash_map)

hash_map.delete(int(input()))
print(hash_map)

print(hash_map.get("key1"))