from typing import Generic, TypeVar, Sequence

T = TypeVar('T')

class LoopedList(Generic[T]):
    def __init__(self, contents: Sequence[T]) -> None:
        self.contents = contents

    def __getitem__(self, i: int) -> T:
        if self.contents and -len(self.contents) <= i < len(self.contents):
            return self.contents[i]
        
        elif self.contents and i >= len(self.contents):
            index = i - len(self.contents)

            while index >= len(self.contents):
                index = index - len(self.contents)

            return self.contents[index]
        
        elif self.contents and i <= -len(self.contents):
            index = i + len(self.contents)

            while index <= -len(self.contents):
                index = index + len(self.contents)

            return self.contents[index]
        
        else:
            raise IndexError

    def __setitem__(self, i: int, t: T) -> None:
        if self.contents and -len(self.contents) <= i < len(self.contents):
            temp: list[T] = []
            for j in range(len(self.contents)):
                if i == j:
                    temp.append(t)
                else:
                    temp.append(self.contents[j]) 
            self.contents = temp

        elif self.contents and i >= len(self.contents):
            index = i - len(self.contents)

            while index >= len(self.contents):
                index = index - len(self.contents)

            temp: list[T] = []
            for j in range(len(self.contents)):
                if index == j:
                    temp.append(t)
                else:
                    temp.append(self.contents[j]) 
            self.contents = temp

        elif self.contents and i <= -len(self.contents):
            index = i + len(self.contents)

            while index <= -len(self.contents):
                index = index + len(self.contents)

            temp: list[T] = []
            for j in range(len(self.contents)):
                if index == j:
                    temp.append(t)
                else:
                    temp.append(self.contents[j]) 
            self.contents = temp
            
        else:
            raise IndexError
    
    def __len__(self) -> int:
        return len(self.contents)
    
    def rotate(self, i: int) -> None:
        if self.contents and -len(self.contents) <= i < len(self.contents):
            temp: list[T] = []

            for j in range(len(self.contents)):
                if j >= i:
                    temp.append(self.contents[j])

            for k in range(len(self.contents)):
                if k < i:
                    temp.append(self.contents[k])                    

            self.contents = temp

        elif self.contents and i >= len(self.contents):
            index = i - len(self.contents)

            while index >= len(self.contents):
                index = index - len(self.contents)

            temp: list[T] = []

            for j in range(len(self.contents)):
                if j >= index:
                    temp.append(self.contents[j])

            for k in range(len(self.contents)):
                if k < index:
                    temp.append(self.contents[k])                    

            self.contents = temp

        elif self.contents and i <= -len(self.contents):
            index = i + len(self.contents)

            while index <= -len(self.contents):
                index = index + len(self.contents)

            temp: list[T] = []

            for j in range(len(self.contents)):
                if j >= index:
                    temp.append(self.contents[j])

            for k in range(len(self.contents)):
                if k < index:
                    temp.append(self.contents[k])                    

            self.contents = temp

        else:
            raise IndexError