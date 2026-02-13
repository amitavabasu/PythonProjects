"""
2 Sum In A Sorted Array
Given an array sorted in non-decreasing order and a target number, find the indices of the two values from the array that sum up to the given target number.

Example
{
"numbers": [1, 2, 3, 5, 10],
"target": 7
}
Output:

[1, 3]
Sum of the elements at index 1 and 3 is 7.

Notes
In case when no answer exists, return an array of size two with both values equal to -1, i.e., [-1, -1].
In case when multiple answers exist, you may return any of them.
The order of the indices returned does not matter.
A single index cannot be used twice.
Constraints:

2 <= array size <= 105
-105 <= array elements <= 105
-105 <= target number <= 105
Array can contain duplicate elements.

"""

def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    n = len(numbers)
    result = [-1, -1]
    if n < 2: return result
    i = 0
    j = n - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            result = [i, j]
            return result
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1
    return result

def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    n = len(numbers)
    result = [-1, -1]
    if n < 2: return result
    map = {}
    for i in range(n):
        number_to_find = target - numbers[i]
        if number_to_find not in map:
            map[numbers[i]] = i
        else:
            return [map[number_to_find], i]
    return result




if __name__ == '__main__':
    numbers = [1, 2, 3, 5, 10]
    target = 7
    print(numbers)
    result = pair_sum_sorted_array(numbers, target)
    print(result)
    result = two_sum(numbers, target)
    print(result)