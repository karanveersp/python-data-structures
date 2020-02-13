def factorial(n):
    if n == 1:  # base case
        return 1
    return n * factorial(n - 1)  # recursive case


def cumulative_sum(n):
    if n == 0:
        return 0
    return n + cumulative_sum(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # print(factorial(10))
    print(fibonacci(8))
    print(cumulative_sum(9))
