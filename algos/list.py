def reverse_list(items, start, end):
    if start >= end:
        return
    items[start], items[end] = items[end], items[start]
    reverse_list(items, start + 1, end - 1)


def binary_search_recursive(items, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    # print(mid)
    # input()
    if items[mid] < key:
        return binary_search_recursive(items, mid + 1, high, key)
    elif items[mid] > key:
        return binary_search_recursive(items, low, mid - 1, key)
    return mid  # items[mid] == key


def binary_search(items, key):
    """Faster than linear if input is sorted"""
    low = 0
    high = len(items) - 1
    while high >= low:
        mid = (high + low) // 2
        if items[mid] < key:
            low = mid + 1
        elif items[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1  # not found


def linear_search(items, key):
    for i, item in enumerate(items):
        if item == key:
            return i
    return -1


if __name__ == "__main__":
    x = [1, 2, 3, 4]
    # reverse_list(x, 0, len(x) - 1)
    # print(x)
    print(binary_search(x, 3))  # 2
