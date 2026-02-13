"""
Problem

Kth Largest In An Array
Given an array of integers, find the k-th largest number in it.

Example One
{
"numbers": [5, 1, 10, 3, 2],
"k": 2
}
Output:

5
Example Two
{
"numbers": [4, 1, 2, 2, 3],
"k": 4
}
Output:

2
Notes
Constraints:

1 <= array size <= 3 * 105
-109 <= array elements <= 109
1 <= k <= array size
"""

import random


def kth_largest_in_an_array(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    n = len(numbers)
    if k >= n:
        return -1
    kth_largest = quick_search(numbers, 0, n-1, n-k)
    return kth_largest

def quick_search(numbers, start, end, k):
    if start <= end:
        partition_index = partition(numbers, start, end)
        if partition_index == k:
            return numbers[partition_index]
        elif partition_index < k:
            return quick_search(numbers, partition_index + 1, end, k)
        else:
            return quick_search(numbers, start, partition_index - 1, k)
    return -1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(numbers, start, end):
    pivot_index = random.randint(start, end)
    swap(numbers, start, pivot_index)
    pivot = numbers[start]
    i = start
    j = i + 1
    while j <= end:
        if numbers[j] < pivot:
            i += 1
            swap(numbers, i, j)
        j = j + 1
    swap(numbers, start, i)
    return i

if __name__ == '__main__':
    k = 4
    array = [4, 1, 2, 2, 3]
    print(kth_largest_in_an_array(array, k))
