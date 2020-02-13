from linked_list import LinkedList, Node


class Queue:
    """Linked List implementation of the Queue ADT"""

    def __init__(self):
        self.list = LinkedList()

    def __len__(self):
        return len(self.list)

    def push(self, data):
        node = Node(data)
        self.list.append(node)  # if this was prepend, we'd have a stack

    def pop(self):
        if self.is_empty():
            raise StopIteration("Attempting to pop from empty queue")
        node = self.list.head.data
        self.list.remove_head()
        return node

    def is_empty(self):
        return self.list.head is None

    def peek(self):
        return self.list.head.data

    def __str__(self):
        return str([data for _, data in self.list.traverse()])


if __name__ == "__main__":
    q = Queue()
    q.push(5)
    q.push(20)
    q.push(10)
    print(q.pop(), "popped")
    print(q.pop(), "popped")
    print(q)
