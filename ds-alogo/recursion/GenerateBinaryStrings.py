"""
Generate Binary Strings Of Length N
Given a number n, generate all possible binary strings of length n.

Example
{
"n": 3
}
Output:

["000", "001", "010", "011", "100", "101", "110", "111"]
Notes
A string consisting of only 0s and 1s is called a binary string.
Return the output list in any order.
Constraints:

1 <= n <= 16
"""


def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    result = []
    get_binary_strings_rec(n, "", result)
    return result

def get_binary_strings_rec(n, prefix, result):
    if n == 0:
        result.append(prefix)
    else:
        get_binary_strings_rec(n - 1, prefix + "0", result)
        get_binary_strings_rec(n - 1, prefix + "1", result)


if __name__ == '__main__':
    n = int(input())
    print(get_binary_strings(n))