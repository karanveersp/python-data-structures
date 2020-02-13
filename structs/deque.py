from linked_list import LinkedList, Node


class Deque:
    def __init__(self):
        self.list = LinkedList()

    def __len__(self):
        return len(self.list)

    def push_front(self, data):
        node = Node(data)
        self.list.prepend(node)

    def push_back(self, data):
        node = Node(data)
        self.list.append(node)

    def pop_front(self):
        if self.is_empty():
            raise StopIteration("Attempting to pop from empty deque")
        data = self.list.head.data
        self.list.remove_head()
        return data

    def pop_back(self):
        if self.is_empty():
            raise StopIteration("Attempting to pop from empty deque")
        data = self.list.tail.data
        self.list.remove_tail()
        return data

    def peek_front(self):
        return self.list.head.data

    def peek_back(self):
        return self.list.tail.data

    def is_empty(self):
        return self.list.head is None

    def __str__(self):
        return str([data for _, data in self.list.traverse()])


if __name__ == "__main__":
    deq = Deque()
    deq.push_front(5)
    deq.push_back(4)
    deq.push_front(3)
    print(deq)
