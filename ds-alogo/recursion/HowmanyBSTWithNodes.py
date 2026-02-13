"""
Problem

How Many Binary Search Trees With N Nodes
Write a function that returns the number of distinct binary search trees that can be constructed with n nodes. For the purpose of this exercise, do solve the problem using recursion first even if you see some non-recursive approaches.

Example One
{
"n": 1
}
Output:

1
Example Two
{
"n": 2
}
Output:

2
Suppose the values are 1 and 2, then the two trees that are possible are

   (2)            (1)
  /       and       \
(1)                  (2)
Example Three
{
"n": 3
}
Output:

5
Suppose the values are 1, 2, 3 then the possible trees are

       (3)
      /
    (2)
   /
(1)

   (3)
  /
(1)
   \
   (2)

(1)
   \
    (2)
      \
       (3)

(1)
   \
    (3)
   /
(2)

   (2)
  /   \
(1)    (3)
Notes
Constraints:

1 <= n <= 16
"""

def how_many_bsts(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    count = how_many_bsts_rec(n)
    return count


def how_many_bsts_rec(n):
    if n == 0 or n == 1: return 1
    else:
        count1 = count2 = 0
        final_count = 0
        for i in range(1, n + 1):
            count1 = how_many_bsts_rec(i - 1)
            count2 = how_many_bsts_rec(n - i)
            total_count = (count1 * count2)
            final_count = final_count + total_count
        return final_count

if __name__ == '__main__':
    print(how_many_bsts(5))