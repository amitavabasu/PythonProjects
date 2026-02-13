"""
Problem

Power
Given a base a and an exponent b. Your task is to find ab. The value could be large enough. So, calculate ab % 1000000007.

Example
{
"a": 2,
"b": 10
}
Output:

1024
Notes
Constraints:

0 <= a <= 104
0 <= b <= 109
a and b together won't be 0
"""

def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    if a == 0: return 0
    if a == 1: return 1
    if b == 0: return 1
    if b == 1: return a

    result = calculate_power_rec(1, a, b, 1000000007)
    return result


def calculate_power_rec(result, a, b, c):
    if b <= 0:
        return result
    if b % 2 == 1:
        result = (result * a) % c
    a = (a * a) % c
    b = b // 2
    return calculate_power_rec(result, a, b, c)


if __name__ == '__main__':
    print(calculate_power(10000, 10000000))
    #print(calculate_power(2, 10))