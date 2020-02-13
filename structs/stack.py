from linked_list import LinkedList, Node


class Stack:
    """Linked List implementation of the Stack ADT"""

    def __init__(self):
        self.list = LinkedList()

    def __len__(self):
        return len(self.list)

    def push(self, data):
        node = Node(data)
        self.list.prepend(node)

    def pop(self):
        if self.is_empty():
            raise StopIteration("Attempting to pop from empty stack")
        data = self.list.head.data
        self.list.remove_head()
        return data

    def peek(self):
        return self.list.head.data

    def is_empty(self):
        return self.list.head is None

    def __str__(self):
        return str([data for _, data in self.list.traverse()])


if __name__ == "__main__":
    st = Stack()
    st.push(5)
    st.push(10)
    print(st)
    print(st.pop(), "popped")
    print(len(st))
    print(st)
