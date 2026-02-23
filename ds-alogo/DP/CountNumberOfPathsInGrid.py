"""
Problem

Unique Paths
Given a grid of size n x m and a robot initially staying at the top-left position, return the number of unique paths for the robot to reach the bottom-right corner of the grid. The robot is allowed to move either down or right at any point in time.

Example One
{
"n": 3,
"m": 2
}
Output:

3
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

Right -> Down -> Down
Down -> Down -> Right
Down -> Right -> Down
Example Two
{
"n": 4,
"m": 1
}
Output:

1
From the top-left corner, there is only one way to reach bottom-right corner:

Down -> Down -> Down
Notes
Return the answer modulo 109 + 7.

Constraints:

1 <= n, m <= 103
.
.
.
.
.

Autocomplete

I/O



00:08:23
"""




def unique_paths(n, m):
    """
    Args:
     n(int32)
     m(int32)
    Returns:
     int32
    """
    arrA = [1] * m
    arrB = [0] * m
    arrB[0] = 1
    for i in range(1, n):
        for j in range(1, m):
            arrB[j] = arrB[j-1] + arrA[j]
        arrA = arrB
        arrB = [0]* m
        arrB[0] = 1
    return arrA[m-1]

if __name__ == "__main__":
    print(unique_paths(5, 5))
