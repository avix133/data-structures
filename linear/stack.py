class Stack:
    """ Array based stack implementation"""

    def __init__(self) -> None:
        self._array = []

    def push(self, value):
        """ Pushing 'D':
            A, B, C
            A, B, C, D """

        self._array.append(value)

    def pop(self):
        """ A, B, C, D
            A, B, C
            :returns last pushed value or None if stack is empty
            removes returned value"""

        return self._array.pop() if self._array else None

    def peek(self):
        """ A, B, C, D
            A, B, C, D
            :returns last pushed value or None if stack is empty"""

        return self._array[-1] if self._array else None

    def __str__(self):
        return str(self._array)

    def __len__(self):
        return len(self._array)

    def __contains__(self, item):
        return item in self._array
