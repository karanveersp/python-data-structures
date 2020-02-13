from linked_list import LinkedList, Node


class Stack:
    """Linked List implementation of the Stack ADT"""

    def __init__(self):
        self.list = LinkedList()

    def push(self, data):
        node = Node(data)
        self.list.prepend(node)

    def pop(self):
        if self.is_empty():
            raise StopIteration("Attempting to pop from empty stack")
        data = self.list.head.data
        self.list.remove_after(None)
        return data

    def peek(self):
        return self.list.head.data

    def is_empty(self):
        return self.list.head is None

    def print(self):
        self.list.print_list()


if __name__ == "__main__":
    st = Stack()
    st.push(5)
    st.push(10)
    st.print()
    print(st.pop(), "popped")
    st.print()
