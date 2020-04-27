class LinkedList:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node

        def __eq__(self, other):
            return self.value == other.value and self.next is other.next

    EMPTY_LIST_ERROR_MSG = 'List is empty!'

    def __init__(self):
        self._head = None

    def add_first(self, value):
        """ A -> B -> C -> D -> None
            E -> A -> B -> C -> D -> None"""
        new_node = self.Node(value=value)

        if self._head:
            new_node.next = self._head
        self._head = new_node

    def add_last(self, value):
        """ A -> B -> C -> D -> None
            A -> B -> C -> D -> E -> None"""
        new_node = self.Node(value)
        last_node = None
        for node in self.__node_iter():
            last_node = node

        if last_node:
            last_node.next = new_node
        else:
            self._head = new_node

    def insert_after(self, item, value):
        """Inserting F after C:
            A -> B -> C -> D -> None
            A -> B -> C -> F -> D -> None"""

        if not self._head:
            raise IndexError(self.EMPTY_LIST_ERROR_MSG)

        node = self._head
        while node and node.value != item:
            node = node.next

        if node:
            node_next = node.next
            node.next = self.Node(value, node_next)
        else:
            raise ValueError(f'No such item {item}')

    def remove(self, value):
        """ Removing C:
            A -> B -> C -> D -> None
            A -> B -> D -> None"""
        if not self._head:
            raise IndexError(self.EMPTY_LIST_ERROR_MSG)

        if self._head.value == value:
            self.poll()
        else:
            previous = self._head
            node = self._head.next
            while node and node.value != value:
                previous = node
                node = node.next
            if node:
                previous.next = node.next
            else:
                raise ValueError(f'No such value: {value}')

    def poll(self):
        """ A -> B -> C -> D -> None
            B -> C -> D -> None"""
        if not self._head:
            return None
        result_node = self._head
        self._head = self._head.next
        return result_node.value

    def pop(self):
        """ A -> B -> C -> D -> None
            A -> B -> C -> None"""
        if not self._head:
            return None

        previous = None
        node = self._head
        while node.next:
            previous = node
            node = node.next
        if previous:
            result_node = previous.next
            previous.next = None
        else:
            result_node = self._head
            self._head = None
        return result_node.value

    def reverse(self):
        """ A -> B -> C -> D -> None
            D -> C -> B -> A -> None"""
        previous = None
        node = self._head
        while node:
            node_next = node.next
            node.next = previous
            previous = node
            node = node_next
        self._head = previous

    def __node_iter(self):
        node = self._head
        while node:
            yield node
            node = node.next

    def __contains__(self, item):
        return any(item == value for value in self)

    def __len__(self):
        return sum(1 for _ in self)

    def __str__(self):
        return "[{}]".format(", ".join(map(str, self)))

    def __iter__(self):
        """:returns values iterator"""
        return iter(map(lambda node: node.value, self.__node_iter()))
