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
    # for each gap, K, we sort K interleaved lists in place.
    # gap value equals number of interleaved lists.
    for gap in gap_values:
        for i in range(0, gap):
            insertion_sort_interleaved(arr, i, gap)
            # input(f"{arr} - gap {gap}")


def partition(arr, i, k):
    mid = (i + (k-i)) // 2
    pivot = arr[mid]

    low, high = i, k
    while True:
        # increment low until a value >= pivot is found
        while arr[low] < pivot:
            low += 1

        # decrement high until a value <= pivot is found
        while arr[high] > pivot:
            high -= 1

        # if zero or one items remaining, all numbers are partitioned. Return h
        if low >= high:
            break
        else:
            # swap arr[l] and arr[h]
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

        return high  # indicating highest index of low partition - not yet sorted


def quicksort(arr, i, k):
    # base case - if 1 or zero elements, partition is sorted
    if i >= k:
        return

    # partition the array - j is the location of last element in low partition
    j = partition(arr, i, k)

    # recursively sort low and high partitions
    quicksort(arr, i, j)
    quicksort(arr, j + 1, k)


def bucket_sort(arr, bucket_count):
    size = len(arr)
    if size < 1:
        return

    buckets = [[] for _ in range(bucket_count)]

    # find max
    max_val = max(arr)

    # put each number in a bucket
    for n in arr:
        index = int(n * (bucket_count - 1) / max_val)
        buckets[index].append(n)

    for b in buckets:
        b.sort()

    # concatenate buckets
    result = []
    for b in buckets:
        result += b

    # copy into original array
    for i, n in enumerate(result):
        arr[i] = n


def radix_get_max_length(arr):
    """Determines the max number of digits found in array elements"""
    max_digits = 0
    for n in arr:
        digit_count = radix_get_length(n)
        if digit_count > max_digits:
            max_digits = digit_count
    return max_digits


def radix_get_length(value):
    """Determines the number of digits in a number"""
    if value == 0:
        return 1

    digits = 0
    while value != 0:
        digits += 1
        value = value // 10
    return digits


def radix_sort(arr):
    buckets = [[] for _ in range(10)]  # base 10

    # find max length in number of digits
    max_digits = radix_get_max_length(arr)

    # start with least significant digit
    pow_10 = 1
    for digit_index in range(max_digits):
        for i in range(len(arr)):
            bucket_index = abs(arr[i] / pow_10) % 10
            buckets[bucket_index].append(arr[i])
        arr_index = 0
        for i in range(10):
            for j in range(len(buckets[i])):
                arr[arr_index] = buckets[i][j]
                arr_index += 1
        pow_10 = 10 * pow_10
        buckets = [[] for _ in range(10)]  # clear all buckets


if __name__ == "__main__":
    # x = [4, 3, 2, 1]
    # # insertion_sort(x)
    # shell_sort(x, (2, 1))
    # print(x)

    x = [4,3,2,1]
    bucket_sort(x, 5)
    print(x)
