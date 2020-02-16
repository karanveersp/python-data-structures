class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._len = 0

    def __len__(self):
        return self._len

    def _find_insertion_position(self, data):
        a = None
        b = self.head
        while b is not None and data > b.data:
            a = b
            b = b.next
        return a

    def insertion_sort(self):
        before_current = self.head
        current = self.head.next

        while current:
            next_node = current.next  # store before updated on current removal
            position = self._find_insertion_position(current.data)

            if position == before_current:
                # means current is already after the proper element
                before_current = current
            else:
                self.remove_after(before_current)
                if position is None:
                    # current is smallest
                    self.prepend(current)
                else:
                    self.insert_after(position, current)
            # advance to next - the preserved original pointer to next for current
            current = next_node

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._len += 1

    def traverse(self):
        node = self.head
        while node:
            yield node, node.data
            node = node.next

    def prepend(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._len += 1

    def insert_after(self, current_node, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_head(self):
        if self.head:
            next_node = self.head.next
            self.head = next_node
            if next_node is None:
                self.tail = None
            self._len -= 1

    def remove_tail(self):
        for node, _ in self.traverse():
            if node.next is self.tail:
                node.next = None
                self.tail = node
                self._len -= 1

    def remove_after(self, current_node):
        if current_node.next:
            node_after = current_node.next.next
            current_node.next = node_after
            if node_after is None:
                # current is new tail
                self.tail = current_node
            self._len -= 1

    def remove(self, data):
        """Removes the node with the first matching data"""
        for n, d in self.traverse():
            if data == d and n is self.head:
                self.remove_head()
            if n.next.data == data:
                self.remove_after(n)

    def append_all(self, *args):
        for node in args:
            self.append(node)

    def prepend_all(self, *args):
        for node in args:
            self.prepend(node)

    def __str__(self):
        return str([data for _, data in self.traverse()])


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion_sort(self):
        current = self.head.next
        while current:
            search_node = current.prev

            while search_node and search_node.data > current.data:
                search_node = search_node.prev

            # remove and re-insert current
            self.remove(current)

            if search_node is None:
                # its the smallest element in the list - becomes head
                current.prev = None
                self.prepend(current)
            else:
                # search_node's data is less than current.data so
                # current should succeed it
                self.insert_after(search_node, current)

            # advance to next node
            current = current.next

    def traverse(self):
        node = self.head
        while node:
            yield node, node.data
            node = node.next

    def traverse_reverse(self):
        node = self.tail
        while node:
            yield node, node.data
            node = node.prev

    def search(self, key):
        node = self.head
        while node:
            if node.data == key:
                return node
            node = node.next
        return None

    def append(self, new_node):
        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def append_all(self, *args):
        for node in args:
            self.append(node)

    def prepend(self, new_node):
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_after(self, current_node, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            # middle insert
            node_after = current_node.next
            new_node.next = node_after
            new_node.prev = current_node
            current_node.next = new_node
            node_after.prev = new_node

    def remove(self, current_node):
        node_after = current_node.next
        node_before = current_node.prev

        if node_after:
            node_after.prev = node_before

        if node_before:
            node_before.next = node_after

        # before/after unlinked from current

        if current_node is self.head:
            self.head = node_after

        if current_node is self.tail:
            self.tail = node_before

    def __str__(self):
        return str([data for _, data in self.traverse()])


if __name__ == "__main__":
    # word_list = LinkedList()
    # a = Node("Python")
    # b = Node("Is")
    # c = Node("Fun!")
    #
    # word_list.append_all(a, b, c)
    #
    # print(word_list)
    num_list = LinkedList()
    num_list.append_all(Node(72), Node(91), Node(53), Node(12))

    print("unsorted", num_list)

    num_list.insertion_sort()

    print("sorted", num_list)
