"""
P-6.33 Give an array-based implementation of a double-ended queue supporting
all of the public behaviors shown in Table 6.4 for the collections.deque
class, including use of the maxlen optional parameter. When a lengthlimited deque is full, provide semantics similar to the collections.deque
class, whereby a call to insert an element on one end of a deque causes an
element to be lost from the opposite side.
"""


class ArrayDeque:
    DEFAULT_DEQUE_CAPACITY = 10

    def __init__(self, maxLen=None):
        self._front = 0
        self._end = 0
        self._maxLen = maxLen
        self._size = 0
        self._data = [None] * ArrayDeque.DEFAULT_DEQUE_CAPACITY

    def __len__(self):
        return self._size

    def add_first(self, e):
        replaced = False
        if self._size >= len(self._data):
            if self._maxLen:
                self._resize(min(self._size * 2, self._maxLen))
            else:
                self._resize(self._size * 2)
        self._front = (self._front - 1) % len(self._data)
        if self._data[self._front] != None:
            replaced = True
        self._data[self._front] = e
        if not replaced:
            self._size += 1

    def add_last(self, e):
        replaced = False
        if self._size >= len(self._data):
            if self._maxLen:
                self._resize(min(self._size * 2, self._maxLen))
            else:
                self._resize(self._size * 2)
        self._end = (self._front + self._size) % len(self._data)
        if self._data[self._end] != None:
            replaced = True
        self._data[self._end] = e
        if not replaced:
            self._size += 1

    def _resize(self, newSize):
        if newSize > len(self._data):
            old = self._data
            self._data = [None] * newSize
            walker = self._front
            for i in range(self._size):
                self._data[i] = old[walker]
                walker = (walker + 1) % len(old)
        self._front = 0
        self._end = self._front + self._size - 1

    def delete_first(self):
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

    def delete_last(self):
        self._data[self._end] = None
        self._end = (self._end - 1) % len(self._data)
        self._size -= 1

    def first(self):
        return self._data[self._front]

    def last(self):
        return self._data[self._end]


if __name__ == "__main__":
    deque = ArrayDeque()
    deque.add_first(3)
    for i in range(10):
        deque.add_last(i + 100)
    deque.add_first(4)
    deque.delete_last()
    deque.delete_last()
    deque.delete_first()
    print("First:", deque.first(), "index", deque._front)
    print("Last:", deque.last(), "index", deque._end)
    # Debugging
    print(deque._data)
