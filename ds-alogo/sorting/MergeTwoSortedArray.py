"""
Merge One Sorted Array Into Another
First array has n positive numbers, and they are sorted in the non-descending order.

Second array has 2n numbers: first n are also positive and sorted in the same way but the last n are all zeroes.

Merge the first array into the second and return the latter. You should get 2n positive integers sorted in the non-descending order.

Example
{
"first": [1, 3, 5],
"second": [2, 4, 6, 0, 0, 0]
}
Output:

[1, 2, 3, 4, 5, 6]
Notes
Constraints:

1 <= n <= 105
1 <= array elements (except those zeroes) <= 2 * 109

"""
def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    n = len(first)
    i = n-1
    j = n-1
    k = 2 * n - 1
    while i >= 0 and j >= 0:
        if first[i] < second[j]:
            second[k] = second[j]
            k -= 1
            j -= 1
        else:
            second[k] = first[i]
            k -= 1
            i -= 1
    while i >= 0:
        second[k] = first[i]
        k -= 1
        i -= 1
    return second

if __name__ == '__main__':
    first = [1, 3, 5]
    second = [2, 4, 6, 0, 0, 0]
    print(first)
    print(second)
    arr = merge_one_into_another(first, second)
    print(arr)