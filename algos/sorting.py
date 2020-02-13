def selection_sort(arr):
    """O(n^2)"""
    n = len(arr)
    for i in range(0, n):
        index_smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[index_smallest]:
                index_smallest = j

        # swap
        arr[i], arr[index_smallest] = arr[index_smallest], arr[i]


def insertion_sort(arr):
    """O(n^2) but for a nearly sorted list O(n)"""
    n = len(arr)
    for i in range(1, n):
        j = i

        # Insert arr[i] into sorted part
        # stopping once arr[i] is in correct position
        while j > 0 and arr[j] < arr[j - 1]:
            # input(f"Swapping {arr[j-1]} and {arr[j]}")
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            # print(arr)
            j -= 1


def insertion_sort_interleaved(arr, start_index, gap):
    """Calling with start_index of 0 and gap of 1 is equivalent to regular insertion sort"""
    for i in range(start_index + gap, len(arr), gap):
        j = i
        while j - gap >= start_index and arr[j] < arr[j - gap]:
            # input(f"Swapping {arr[j-gap]} with {arr[j]}")
            arr[j], arr[j-gap] = arr[j-gap], arr[j]
            j -= gap


def shell_sort(arr, gap_values):
    """Choosing gap values that are powers of 2 minus 1 in descending order gives O(n^3/2)"""
    for gap in gap_values:
        for i in range(0, gap):
            insertion_sort_interleaved(arr, i, gap)
            # input(f"{arr} - gap {gap}")


def partition(arr, i, k):
    mid = (i + (k-i)) // 2
    pivot = arr[mid]

    low, high = i, k
    done = False
    while not done:
        # increment low until a value greater than pivot is found
        while arr[low] < pivot:
            low += 1

        # decrement high until a value less than pivot is found
        while arr[high] > pivot:
            high -= 1

        # if zero or one items remaining, all numbers are partitioned. Return h
        if low >= high:
            done = True
        else:
            # swap arr[l] and arr[h]
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

        return high


if __name__ == "__main__":
    x = [4, 3, 2, 1]
    # insertion_sort(x)
    shell_sort(x, (2, 1))
    print(x)
