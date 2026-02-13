"""
Problem

Online Median
Given a list of numbers, the task is to insert these numbers into a stream and find the median of the stream after each insertion. If the median is a non-integer, consider it’s floor value.

The median of a sorted array is defined as the middle element when the number of elements is odd and the mean of the middle two elements when the number of elements is even.

Example
{
"stream": [3, 8, 5, 2]
}
Output:

[3, 5, 5, 4]
Iteration	Stream	Sorted Stream	Median
1	[3]	[3]	3
2	[3, 8]	[3, 8]	(3 + 8) / 2 => 5
3	[3, 8, 5]	[3, 5, 8]	5
4	[3, 8, 5, 2]	[2, 3, 5, 8]	(3 + 5) / 2 => 4
Notes
Constraints:

1 <= length of stream <= 105
1 <= any value in the stream <= 105
The stream can contain duplicates.
"""
import heapq

def online_median(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    n = len(stream)
    if n == 0: return 0
    result = []
    left_heap = [] # max (use negative)
    right_heap = [] # min
    median = 0
    for i in range(n):
        if i == 0:
            median = stream[i]
            heapq.heappush(left_heap, -stream[i])
        elif i == 1:
            if stream[i] >= -left_heap[0]:
                heapq.heappush(right_heap, stream[i])
            else:
                heapq.heappush(right_heap, -heapq.heappushpop(left_heap, -stream[i]))
            median = ((-left_heap[0]) + right_heap[0]) // 2
        else:
            if i % 2 == 1:
                if len(left_heap) > len(right_heap):
                    if stream[i] >= -left_heap[0]:
                        heapq.heappush(right_heap, stream[i])
                    else:
                        heapq.heappush(right_heap, -heapq.heappushpop(left_heap, -stream[i]))
                else:
                    if stream[i] >= -left_heap[0]:
                        heapq.heappush(left_heap, -heapq.heappushpop(right_heap, stream[i]))
                    else:
                        heapq.heappush(left_heap, -stream[i])
                median = ((-left_heap[0]) + right_heap[0]) // 2
            else:
                if stream[i] >= -left_heap[0]:
                    heapq.heappush(right_heap, stream[i])
                else:
                    heapq.heappush(left_heap, -stream[i])
                if len(left_heap) > len(right_heap):
                    median = -left_heap[0]
                else:
                    median = right_heap[0]
        result.append(median)
    return result







if __name__ == '__main__':
    array = [1000000000, 999999997]
    print(online_median(array))
