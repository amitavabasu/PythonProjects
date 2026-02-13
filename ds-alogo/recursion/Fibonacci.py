

def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    if n == 0: return 1
    return fib(n, 0, 1)


def fib(n, i, j):
    if n == 0:
        return i
    else:
        return fib(n-1, j, i+j)



if __name__ == '__main__':
    print(find_fibonacci(8))