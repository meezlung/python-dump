class CapsLock:
    def __init__(self, string: str) -> None:
        self.string = string

    def uppercase(self) -> str:
        return self.string.upper()
    
c = CapsLock('abc')
print(c.uppercase())