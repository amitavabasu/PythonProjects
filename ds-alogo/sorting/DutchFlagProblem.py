"""
Given some balls of three colors arranged in a line, rearrange them such that all the red balls go first, then green and then blue ones.

Do rearrange the balls in place. A solution that simply counts colors and overwrites the array is not the one we are looking for.

This is an important problem in search algorithms theory proposed by Dutch computer scientist Edsger Dijkstra. Dutch national flag has three colors (albeit different from ones used in this problem).

Example
{
"balls": ["G", "B", "G", "G", "R", "B", "R", "G"]
}
Output:

["R", "R", "G", "G", "G", "G", "B", "B"]
There are a total of 2 red, 4 green and 2 blue balls. In this order they appear in the correct output.

Notes
Constraints:

1 <= n <= 100000
Do this in ONE pass over the array, NOT TWO passes
Solution is only allowed to use constant extra memory



"""

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def dutch_flag_sort(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    if arr is None or len(arr) <2 : return arr
    n = len(arr)
    l = 0
    m = 0
    r = n - 1

    while m <= r:
        if arr[m] == "R":
            swap(arr, m, l)
            m += 1
            l += 1
        elif arr[m] == "G":
            m += 1
        else:
            swap(arr, m, r)
            r -= 1
    return arr









    return []


if __name__ == '__main__':
    array = ["G", "B", "G", "G", "R", "B", "R", "G"]
    print(array)
    arr1 = dutch_flag_sort(array)
    print(array)