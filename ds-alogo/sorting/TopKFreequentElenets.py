"""
Problem

Top K Frequent Elements
Given an integer array and a number k, find the k most frequent elements in the array.

Example One
{
"arr": [1, 2, 3, 2, 4, 3, 1],
"k": 2
}
Output:

[3, 1]
Example Two
{
"arr": [1, 2, 1, 2, 3, 1],
"k": 1
}
Output:

[1]
Notes
If multiple answers exist, return any.
The order of numbers in the output array does not matter.
Constraints:

1 <= length of the given array <= 3 * 105
0 <= array element <= 3 * 105
1 <= k <= number of unique elements in the array
"""
def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    map = {}
    for num in arr:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True)
    top_k_frequent = (item[0] for item in sorted_map[:k])
    return list(top_k_frequent)



if __name__ == '__main__':
    arr = [1, 2, 1, 2, 3, 1]
    k = 1

    print(find_top_k_frequent_elements(arr, k))
