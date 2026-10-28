from stack import Stack

class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, item: int):
        self._queue.append(item)

    def dequeue(self)->int:
        if len(self._queue) >=1:
            return self._queue.pop(0)
        raise IndexError

class Queue2:
    def __init__(self):
        self._left = Stack()
        self._right = Stack()

    def enqueue(self, item: int):
        self._left.push(item)

    def dequeue(self)->int:
        if not self._right.is_empty():
            return self._right.pop()
        elif not self._left.is_empty():
            while not self._left.is_empty():
                self._right.push(self._left.pop())
            return self._right.pop()
        raise IndexError

    def is_empty(self)->bool:
        return self._left.is_empty() and self._right.is_empty()
