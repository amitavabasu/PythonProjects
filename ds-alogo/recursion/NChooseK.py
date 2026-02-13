"""
Problem

N Choose K Combinations
Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.

Example One
{
"n": 5,
"k": 2
}
Output:

[
[1, 2],
[1, 3],
[1, 4],
[1, 5],
[2, 3],
[2, 4],
[2, 5],
[3, 4],
[3, 5],
[4, 5]
]
Example Two
{
"n": 6,
"k": 6
}
"""
def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    results = []
    used_numbers = []
    combinations(n, k, 1, used_numbers, results)
    return results

def combinations(n, k, current_number, used_numbers, results):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
     :param results:
     :param used_numbers:
     :param current_number:
    """
    if len(used_numbers) == k:
        results.append(list(used_numbers))
        return
    if current_number == n + 1:
        return
    else:
        used_numbers.append(current_number)
        combinations(n, k, current_number + 1, used_numbers, results)
        used_numbers.pop()
        combinations(n, k, current_number + 1, used_numbers, results)
        return


if __name__ == '__main__':
    n = 5
    k = 2
    print(find_combinations(n, k))