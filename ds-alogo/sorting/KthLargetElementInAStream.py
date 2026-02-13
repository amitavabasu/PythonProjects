"""
Problem

Kth Largest In A Stream
Given an initial list along with another list of numbers to be appended with the initial list and an integer k, return an array consisting of the k-th largest element after adding each element from the first list to the second list.

Example
{
"k": 2,
"initial_stream": [4, 6],
"append_stream": [5, 2, 20]
}
Output:

[5, 5, 6]
Append	Stream	Sorted Stream	2nd largest
5	[4, 6, 5]	[4, 5, 6]	5
2	[4, 6, 5, 2]	[2, 4, 5, 6]	5
20	[4, 6, 5, 2, 20]	[2, 4, 5, 6, 20]	6
Notes
The stream can contain duplicates.
Constraints:

1 <= length of both lists <= 105
1 <= k <= length of initial list + 1
0 <= any value in the list <= 109
"""
import heapq

def kth_largest(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    n = len(initial_stream)
    if k < 1 or k > n + 1: return []
    min_heap = []
    for num in initial_stream:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappushpop(min_heap, num)
    result = []
    for num in append_stream:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0] and len(min_heap) == k:
            heapq.heappushpop(min_heap, num)

        result.append(min_heap[0])
    return result


if __name__ == '__main__':
    k = 2
    initial_stream = [4, 6]
    append_stream = [5, 2, 20]
    print(kth_largest(k, initial_stream, append_stream))



