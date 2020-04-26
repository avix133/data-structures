import pytest

from linear.linked_list import LinkedList


class TestLinkedList:
    def setup_method(self):
        """[12, 8, 2, 5]"""
        self.prepared_linked_list = LinkedList()
        self.prepared_linked_list.add_first(5)
        self.prepared_linked_list.add_first(2)
        self.prepared_linked_list.add_first(8)
        self.prepared_linked_list.add_first(12)

        assert list(self.prepared_linked_list) == [12, 8, 2, 5]

    def test_add_first(self):
        linked_list = LinkedList()

        linked_list.add_first(1)
        assert list(linked_list) == [1]

        linked_list.add_first(3)
        assert list(linked_list) == [3, 1]

        linked_list.add_first(5)
        assert list(linked_list) == [5, 3, 1]

        linked_list.add_first(4)
        assert list(linked_list) == [4, 5, 3, 1]

    def test_add_last(self):
        linked_list = LinkedList()

        linked_list.add_last(1)
        assert list(linked_list) == [1]

        linked_list.add_last(3)
        assert list(linked_list) == [1, 3]

        linked_list.add_last(5)
        assert list(linked_list) == [1, 3, 5]

        linked_list.add_last(4)
        assert list(linked_list) == [1, 3, 5, 4]

    def test_insert_after(self):
        self.prepared_linked_list.insert_after(2, 4)
        assert list(self.prepared_linked_list) == [12, 8, 2, 4, 5]

        self.prepared_linked_list.insert_after(2, 3)
        assert list(self.prepared_linked_list) == [12, 8, 2, 3, 4, 5]

        self.prepared_linked_list.insert_after(12, 1)
        assert list(self.prepared_linked_list) == [12, 1, 8, 2, 3, 4, 5]

        self.prepared_linked_list.insert_after(5, 50)
        assert list(self.prepared_linked_list) == [12, 1, 8, 2, 3, 4, 5, 50]

        with pytest.raises(ValueError):
            self.prepared_linked_list.insert_after(16, 40)

        linked_list = LinkedList()
        with pytest.raises(IndexError):
            linked_list.insert_after(5, 12)

        linked_list.add_first(3)
        linked_list.insert_after(3, 4)
        assert list(linked_list) == [3, 4]

    def test_remove_first(self):
        self.prepared_linked_list.remove_first()
        assert list(self.prepared_linked_list) == [8, 2, 5]

        self.prepared_linked_list.remove_first()
        assert list(self.prepared_linked_list) == [2, 5]

        self.prepared_linked_list.remove_first()
        assert list(self.prepared_linked_list) == [5]

        self.prepared_linked_list.remove_first()
        assert list(self.prepared_linked_list) == []

        with pytest.raises(IndexError):
            self.prepared_linked_list.remove_first()

    def test_remove_last(self):
        self.prepared_linked_list.remove_last()
        assert list(self.prepared_linked_list) == [12, 8, 2]

        self.prepared_linked_list.remove_last()
        assert list(self.prepared_linked_list) == [12, 8]

        self.prepared_linked_list.remove_last()
        assert list(self.prepared_linked_list) == [12]

        self.prepared_linked_list.remove_last()
        assert list(self.prepared_linked_list) == []

        with pytest.raises(IndexError):
            self.prepared_linked_list.remove_last()

    def test_remove(self):
        self.prepared_linked_list.remove(2)
        assert list(self.prepared_linked_list) == [12, 8, 5]

        self.prepared_linked_list.remove(12)
        assert list(self.prepared_linked_list) == [8, 5]

        with pytest.raises(ValueError):
            self.prepared_linked_list.remove(12)

        assert list(self.prepared_linked_list) == [8, 5]

        self.prepared_linked_list.remove(5)
        assert list(self.prepared_linked_list) == [8]

        self.prepared_linked_list.remove(8)
        assert list(self.prepared_linked_list) == []

        with pytest.raises(IndexError):
            self.prepared_linked_list.remove(8)

    def test_reverse(self):
        self.prepared_linked_list.reverse()
        assert list(self.prepared_linked_list) == [5, 2, 8, 12]

        linked_list = LinkedList()
        linked_list.reverse()
        assert list(linked_list) == []

        linked_list.add_first(5)
        linked_list.reverse()
        assert list(linked_list) == [5]

    def test_contains(self):
        assert 12 in self.prepared_linked_list
        assert 2 in self.prepared_linked_list
        assert 5 in self.prepared_linked_list
        assert 8 in self.prepared_linked_list

        assert 11 not in self.prepared_linked_list
        assert 28 not in self.prepared_linked_list

        linked_list = LinkedList()
        assert 5 not in linked_list

        linked_list.add_first(5)
        assert 5 in linked_list

    def test_len(self):
        assert len(self.prepared_linked_list) == 4

        self.prepared_linked_list.remove_last()
        assert len(self.prepared_linked_list) == 3

        self.prepared_linked_list.remove_first()
        assert len(self.prepared_linked_list) == 2

        self.prepared_linked_list.remove_first()
        assert len(self.prepared_linked_list) == 1

        self.prepared_linked_list.remove_last()
        assert len(self.prepared_linked_list) == 0

    def test_iter(self):
        assert next(iter(self.prepared_linked_list)) == 12

        iterator = iter(self.prepared_linked_list)
        assert next(iterator) == 12
        assert next(iterator) == 8
        assert next(iterator) == 2
        assert next(iterator) == 5
        with pytest.raises(StopIteration):
            next(iterator)
