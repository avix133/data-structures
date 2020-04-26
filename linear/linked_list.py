class LinkedList:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node

        def __eq__(self, other):
            return self.value == other.value and self.next == other.next

    EMPTY_LIST_ERROR_MSG = 'List is empty!'

    def __init__(self):
        self.__head = None

    def add_first(self, value):
        """ A -> B -> C -> D -> None
            E -> A -> B -> C -> D -> None"""
        new_node = self.Node(value=value)

        if self.__head:
            new_node.next = self.__head
        self.__head = new_node

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
            self.__head = new_node

    def insert_after(self, item, value):
        """Inserting F after C:
            A -> B -> C -> D -> None
            A -> B -> C-> -> F -> D -> None"""

        if not self.__head:
            raise IndexError(self.EMPTY_LIST_ERROR_MSG)

        node = self.__head
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
        if not self.__head:
            raise IndexError(self.EMPTY_LIST_ERROR_MSG)

        if self.__head.value == value:
            self.remove_first()
        else:
            previous = self.__head
            node = self.__head.next
            while node and node.value != value:
                previous = node
                node = node.next
            if node:
                previous.next = node.next
            else:
                raise ValueError(f'No such value: {value}')

    def remove_first(self):
        """ A -> B -> C -> D -> None
            B -> C -> D -> None"""
        if not self.__head:
            raise IndexError(self.EMPTY_LIST_ERROR_MSG)
        self.__head = self.__head.next

    def remove_last(self):
        """ A -> B -> C -> D -> None
            A -> B -> C -> None"""
        if not self.__head:
            raise IndexError(self.EMPTY_LIST_ERROR_MSG)

        previous = None
        node = self.__head
        while node.next:
            previous = node
            node = node.next
        if previous:
            previous.next = None
        else:
            self.__head = None

    def reverse(self):
        """ A -> B -> C -> D -> None
            D -> C -> B -> A -> None"""
        previous = None
        node = self.__head
        while node:
            node_next = node.next
            node.next = previous
            previous = node
            node = node_next
        self.__head = previous

    def __node_iter(self):
        node = self.__head
        while node:
            yield node
            node = node.next

    def __contains__(self, item):
        for value in self:
            if item == value:
                return True
        return False

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def __str__(self):
        return "[{}]".format(", ".join(map(str, self)))

    def __iter__(self):
        """:returns values iterator"""
        return iter(map(lambda node: node.value, self.__node_iter()))

