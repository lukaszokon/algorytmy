class Queue:

    class _Element:
        def __init__(self, prev, value):
            self.value = value
            self.prev = prev

    def __init__(self):
        self._first = None
        self._last = None

    def insert(self, value):
        new_element = self._Element(None, value)
        if not self._first:
            self._first = new_element
            self._last = new_element
        else:
            self._first.prev = new_element
            self._first = new_element

    def delete(self):
        if not self._last:
            return None
        else:
            temp_element = self._last
            self._last = temp_element.prev
            return temp_element.value

class Stack:
    class _Element:
        def __init__(self, value, prev):
            self.value = value
            self.prev = prev

    def __init__(self):
        self._last = None

    def push(self, value):
        if not self._last:
            new_element = self._Element(value, None)
        else:
            new_element = self._Element(value, self._last)
        self._last = new_element

    def pop(self):
        if not self._last:
            return None

        element = self._last
        self._last = self._last.prev
        return element.value


from collections import deque

if __name__ == '__main__':

    queue = Queue()
    for i in range(5):
        print(i + 1)
        queue.insert(i + 1)

    for i in range(5):
        print(queue.delete())
