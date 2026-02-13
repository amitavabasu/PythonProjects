"""
Problem

Permute Array Of Unique Integers
Given an array of unique numbers, return in any order all its permutations.

Example
{
"arr": [1, 2, 3]
}
Output:

[
[1, 2, 3],
[1, 3, 2],
[2, 1, 3],
[2, 3, 1],
[3, 2, 1],
[3, 1, 2]
]
Notes
Constraints:

1 <= size of the input array <= 9
0 <= any array element <= 99
"""

def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    prefix = []
    result = []
    get_permutations_rec(prefix, arr, result)
    return result

def get_permutations_rec(prefix, arr, result):
    if arr is None or len(arr) == 0:
        result.append(prefix)
    else:
        for i in range(len(arr)):
            p = prefix.copy()
            p.append(arr[i])
            a = arr[:i].copy()
            a.extend(arr[i+1:])
            get_permutations_rec(p, a, result)

if __name__ == '__main__':
    arr = [1, 2, 3]
    print(get_permutations(arr))