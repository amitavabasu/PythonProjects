"""
3 Sum
Given an integer array arr of size n, find all magic triplets in it.

Magic triplet is a group of three numbers whose sum is zero.

Note that magic triplets may or may not be made of consecutive numbers in arr.

Example
{
"arr": [10, 3, -4, 1, -6, 9]
}
Output:

["10,-4,-6", "3,-4,1"]
Notes
Function must return an array of strings. Each string (if any) in the array must represent a unique magic triplet and strictly follow this format: "1,2,-3" (no whitespace, one comma between numbers).
Order of the strings in the array is insignificant. Order of the integers in any string is also insignificant. For example, if ["1,2,-3", "1,-1,0"] is a correct answer, then ["0,1,-1", "1,-3,2"] is also a correct answer.
Triplets that only differ by order of numbers are considered duplicates, and duplicates must not be returned. For example, if "1,2,-3" is a part of an answer, then "1,-3,2", "-3,2,1" or any permutation of the same numbers may not appear in the same answer (though any one of them may appear instead of "1,2,-3").
Constraints:

1 <= n <= 2000
-1000 <= any element of arr <= 1000
arr may contain duplicate numbers
arr is not necessarily sorted
"""

def find_zero_sum(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    if arr is None or len(arr) < 3: return []
    n = len(arr)
    arr.sort(reverse=True)
    result = set()
    for i in range(n):
        x = arr[i]
        j = i + 1
        k = n - 1
        while j < k:
            if x + arr[j] + arr[k] == 0:
                result.add(f"{x},{arr[j]},{arr[k]}")
                j += 1
            elif x + arr[j] + arr[k] < 0:
                k -= 1
            else:
                j += 1

    return list(result)


def four_sum(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    if arr is None or len(arr) < 4: return []
    n = len(arr)
    arr.sort(reverse=True)
    result = []
    result_set = set()
    current = [0, 0, 0, 0]
    for i in range(n):
        x = arr[i]
        for j in range(i + 1, n):
            y = arr[j]
            k = j + 1
            l = n - 1
            while k < l:
                if x + y + arr[k] + arr[l] == target:
                    current[0] = x
                    current[1] = y
                    current[2] = arr[k]
                    current[3] = arr[l]
                    current.sort()
                    result_set.add(tuple(current))
                    k += 1
                elif x + y + arr[k] + arr[l] < target:
                    l -= 1
                else:
                    k += 1
    for element in result_set:
        result.append(list(element))
    return result

if __name__ == '__main__':
    arr = [0, 0, 0, 0, 0, 0]
    print(arr)
    result = find_zero_sum(arr)
    print(result)
    arr = [0, 0, 1, 3, 2, -1]
    print(arr)
    result = four_sum(arr, 3)
    print(result)