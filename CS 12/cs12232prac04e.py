from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self.stack: list[T] = []

    def push(self, value: T) -> None:
        self.stack.append(value)

    def pop(self) -> T:
        if len(self.stack) == 0:
            raise ValueError
        return self.stack.pop()
    
    def clear(self) -> None:
        self.stack.clear()

    def __len__(self, s: int) -> int:
        return len(self.stack)
    
class SnoopingStack(Stack[T]):
    def __init__(self):
        super().__init__()
        self.operations_history: list[T | None] = []

    def push(self, value: T) -> None:
        super().push(value)
        self.operations_history.append(value)
    
    def pop(self) -> T:
        if len(self.stack) == 0:
            raise ValueError
        popped = super().pop()
        
        if len(self.stack) != 0:
            self.operations_history.append(self.stack[-1])
        else:
            self.operations_history.append(None)
        return popped
    
    def clear(self) -> None:
        self.operations_history.append(None)
        super().clear()

    def history(self) -> list[T | None]:
        return self.operations_history
    
    def __len__(self) -> int:
        return len(self.stack)