"""
3 Sum Smaller
Given a list of numbers, count the number of triplets having a sum less than a given target.

Example One
{
"target": 4,
"numbers": [5, 0, -1, 3, 2]
}
Output:

2
{numbers[1], numbers[2], numbers[3]} and {numbers[1], numbers[2], numbers[4]} are the triplets having sum less than 4.

Example Two
{
"target": 7,
"numbers": [2, 2, 2, 1]
}
Output:

4
{numbers[0], numbers[1], numbers[2]}, {numbers[0], numbers[1], numbers[3]}, {numbers[0], numbers[2], numbers[3]} and {numbers[1], numbers[2], numbers[3]} are the triplets having sum less than 7.

Notes
The original array's indexes identify a triplet. Therefore, any two triplets will differ if they are denoted by a different triplet of indexes, even if the values present at those indexes are the same. Please observe Example Two for more details on this.

Constraints:

3 <= size of the input list <= 103
-105 <= any element of the input list <= 105
-109 <= target number <= 109
"""

def count_triplets(target, numbers):
    """
    Args:
     target(int32)
     numbers(list_int32)
    Returns:
     int32
    """
    if len(numbers) < 3: return 0
    n = len(numbers)
    numbers.sort()
    count = 0
    for i in range(n - 2):
        if numbers[i] + numbers[i+1] + numbers[i+2]>= target: break
        j = i + 1
        while j < n - 1:
            if numbers[i] + numbers[j] + numbers[j+1] >= target: break
            k = n - 1
            while j < k:
                if numbers[i] + numbers[j] + numbers[k] >= target:
                    k -= 1
                else:
                    count += k - j
                    break
            j += 1
    return count

if __name__ == '__main__':
    numbers = [5, 0, -1, 3, 2]
    print(numbers)
    result = count_triplets(4, numbers)
    print(result)
    numbers = [2, 2, 2, 1]
    print(numbers)
    result = count_triplets(7, numbers)
    print(result)