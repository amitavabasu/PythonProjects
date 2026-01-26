""""
Constraints:

1 <= length of the given list <= 4 * 10^5 = 400,000
-4 * 105 <= number in the list <= 4 * 10^5 = 400,000
"""
def counting_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    n = len(arr)
    if n <= 1: return arr
    maximum = max(arr)
    minimum = min(arr)
    count_range = maximum - minimum + 1
    counts = [0] * count_range

    for num in arr:
        counts[num - minimum] += 1

    sort_idx = 0
    for i in range(count_range):
        while counts[i] > 0:
            arr[sort_idx] = minimum + i
            sort_idx += 1
            counts[i] -= 1
    return arr

if __name__ == '__main__':
    arr1 = [1,2,3,4,5,6,7,8,9,10,11,0,15,17,16]
    print(arr1)
    arr1 = counting_sort(arr1)
    print(arr1)
