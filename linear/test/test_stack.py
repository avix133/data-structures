from linear.stack import Stack


class TestStack:
    def setup_method(self):
        self.stack = Stack()
        self.stack.push(5)
        self.stack.push(3)
        self.stack.push(1)

    def test_pop(self):
        assert self.stack.pop() == 1
        assert self.stack.pop() == 3
        assert self.stack.pop() == 5
        assert not self.stack.pop()

    def test_peek(self):
        assert self.stack.peek() == 1
        assert self.stack.peek() == 1
        self.stack.pop()
        assert self.stack.peek() == 3
        self.stack.pop()
        assert self.stack.peek() == 5
        self.stack.pop()
        assert not self.stack.peek()
