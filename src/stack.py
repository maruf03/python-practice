class Stack:
    def __init__(self):
        self._stack = []

    def pop(self)->int:
        if len(self._stack) >=1:
            return self._stack.pop()
        raise IndexError

    def push(self, item:int):
        self._stack.append(item)

    def is_empty(self)->bool:
        return len(self._stack) == 0
