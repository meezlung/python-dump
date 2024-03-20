from typing import Generic, TypeVar, MutableMapping

K = TypeVar('K')
V = TypeVar('V')

class BiDict(Generic[K, V]):
    def __init__(self, contents: MutableMapping[K, V]) -> None:
        self.contents = contents

    def __getitem__(self, k: K) -> V:
        if not self.contents[k]:
            raise KeyError
        return self.contents[k]
    
    def __setitem__(self, k: K, v: V) -> None:
        self.contents[k] = v
    
    def __len__(self) -> int:
        return len(self.contents)
    
    def pop(self, k: K) -> V:
        if not self.contents[k]:
            raise KeyError
        value: V = self.contents[k]
        del self.contents[k]
        return value
    
    def keys_with_value(self, v: V) -> set[K]:
        keys_set = set()

        for key in self.contents:
            if self.contents[key] == v:
                keys_set.add(key)

        return keys_set

    