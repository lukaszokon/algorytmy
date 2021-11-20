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


if __name__ == '__main__':

    stack = Stack()
    for i in range(5):
        print(i + 1)
        stack.push(i + 1)

    for i in range(5):
        print(stack.pop())
