def get_parent_index(i):
    return (i - 1) // 2


def get_left_child_index(i):
    return 2 * i + 1


def get_right_child_index(i):
    return 2 * i + 2


class MaxHeap:
    def __init__(self, arr=None):
        self.heap_array = arr if arr else []

    def percolate_up(self, index):
        while index > 0:
            # compute parent node index
            parent_index = get_parent_index(index)

            # check for violation of max heap property
            if self.heap_array[index] <= self.heap_array[parent_index]:
                # no violation, so percolate up is done
                return

            # we swap
            temp = self.heap_array[index]
            self.heap_array[index] = self.heap_array[parent_index]
            self.heap_array[parent_index] = temp

            # continue the loop from parent node
            index = parent_index

    def percolate_down(self, index):
        child_index = get_left_child_index(index)
        val = self.heap_array[index]

        while child_index < len(self.heap_array):
            # find the max among the node and the node's children
            max_val = val
            max_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] > max_val:
                    max_val = self.heap_array[i + child_index]
                    max_index = i + child_index
                i += 1

            # check for violation of max heap property
            if max_val == val:
                return

            temp = self.heap_array[index]
            self.heap_array[index] = self.heap_array[max_index]
            self.heap_array[max_index] = temp

            # continue loop from larger child node
            index = max_index
            child_index = get_left_child_index(index)

    def insert(self, val):
        """adds val to end, then uses percolate up to restore the max heap property"""
        self.heap_array.append(val)
        self.percolate_up(len(self.heap_array) - 1)

    def remove(self):
        """always returns max val at index 0"""
        max_val = self.heap_array[0]  # save max

        # move the last item in the array to index 0
        replaced_val = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replaced_val

            # percolate down to restore max heap property
            self.percolate_down(0)

        return max_val


if __name__ == "__main__":
    pass
