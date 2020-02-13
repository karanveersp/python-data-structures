class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def print_list(self):
        for _, data in self.traverse():
            print(data)
        print()


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

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

    def remove_after(self, current_node):
        # special case - remove head
        if current_node is None and self.head:
            next_node = self.head.next
            self.head = next_node
            if next_node is None:
                # we removed last item
                self.tail = None
        elif current_node.next:
            node_after = current_node.next.next
            current_node.next = node_after
            if node_after is None:
                # current is new tail
                self.tail = current_node

    def print_list(self):
        for _, data in self.traverse():
            print(data)
        print()


if __name__ == "__main__":
    word_list = DoublyLinkedList()
    a = Node("Python")
    b = Node("Is")
    c = Node("Fun!")

    [word_list.append(node) for node in (a, b, c)]

    word_list.print_list()
