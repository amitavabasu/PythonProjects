"""
Problem

Intersection Of Three Sorted Arrays
Given three arrays sorted in the ascending order, return their intersection sorted array in the ascending order.

Example One
{
"arr1": [2, 5, 10],
"arr2": [2, 3, 4, 10],
"arr3": [2, 4, 10]
}
Output:

[2, 10]
Example Two
{
"arr1": [1, 2, 3],
"arr2": [],
"arr3": [2, 2]
}
Output:

[-1]
Example Three
{
"arr1": [1, 2, 2, 2, 9],
"arr2": [1, 1, 2, 2],
"arr3": [1, 1, 1, 2, 2, 2]
}
Output:

[1, 2, 2]
Notes
If the intersection is empty, return an array with one element -1.
Constraints:

0 <= length of each given array <= 105
0 <= any value in a given array <= 2 * 106
"""


def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)
    common = set()
    i = 0
    j = 0
    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
            common.add(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    arr4 = sorted(list(common))
    common = set()
    n4 = len(arr4)
    i = 0
    j = 0
    while i < n4 and j < n3:
        if arr4[i] == arr3[j]:
            common.add(arr4[i])
            i += 1
            j += 1
        elif arr4[i] < arr3[j]:
            i += 1
        else:
            j += 1
    if len(common) == 0:
        return [-1]
    else:
        return list(common)


if __name__ == '__main__':
    arr1 = [2, 5, 10]
    arr2 = [2, 3, 4, 10]
    arr3 = [2, 4, 10]
    print(find_intersection(arr1, arr2, arr3))


