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


class Mylist:
    class _Element:

        def __init__(self, value, next, prev):
            self.value = value
            self.next = next
            self.prev = prev

    def __init__(self):
        self._head = None
        self._tail = None

    def append(self, value):
        new_element = self._Element(value, None, None)
        if not self._head:
            self._head = new_element
            self._tail = new_element
        else:
            new_element.prev = self._tail
            self._tail.next = new_element
            self._tail = new_element

    def delete(self):
        deleting_element = self._head
        new_head = deleting_element.next
        new_head.prev = None
        self._head = new_head
        return deleting_element.value

    def remove(self, value):
        iterator = self._head
        if iterator.value == value:
            self._head = iterator.next
            return 0
        while iterator.next and iterator.next.value != value:
            iterator = iterator.next

        if iterator.next.value != value:
            return 1
        else:
            if iterator.next == self._tail:
                self._tail = iterator
            iterator.next = iterator.next.next
            return 0


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

    my_list = Mylist()
    for i in range(5):
        print(i + 1)
        my_list.append(i + 1)

    # my_list.remove(4)
    # my_list.remove(1)
    # my_list.remove(5)
    # print()

    # for i in range(5):
    #     print(queue.delete())
