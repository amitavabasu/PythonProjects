def ncr(n, r):
    """
    Args:
     n(int32)
     r(int32)
    Returns:
     int32
    """
    if n == 0 or r == 0 or n == r: return 1
    arrA = [0] * (n+1)
    arrB = [0] * (n+1)
    arrB[0] = 1
    arrB[1] = 1
    for i in range(1, n):
        arrA[0] = 1
        for j in range(1, i+1):
            arrA[j] = arrB[j] + arrB[j - 1]
        arrA[i+1] = 1
        arrB = arrA
        arrA = [0]* (n+1)

    return arrB[r] % 1000000007


if __name__ == '__main__':
    print(ncr(1000, 500))