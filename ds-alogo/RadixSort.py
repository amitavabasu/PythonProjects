

def radix_sort_helper(arr, pow):
    n = len(arr)
    output = [0] * n
    count_array = [0] * 10
    for i in range(n):
        counter_index = (arr[i] // pow) % 10
        count_array[counter_index] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1] #<-- converting count_array to index based i.e. count_array[count_index-1] = index in actual output

    i = n - 1
    while i >= 0:
        index = (arr[i] // pow) % 10
        output[count_array[index] - 1] = arr[i] #<-- minus one as this is a counter starting from 1
        count_array[index] -= 1 #<-- reduce counter as one input is placed at right spot
        i -= 1 #<-- go right to left
    for i in range(len(arr)): #<-- From output array to arr
        arr[i] = output[i]
    return arr


def radix_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    max_val = max(arr)
    p = 1
    while (max_val // p) > 0:
        radix_sort_helper(arr, p)
        p *= 10
    return arr


if __name__ == '__main__':
    arr1 = [1,2,3,4,5,6,7,8,9,10,11,0,15,17,16]
    print(arr1)
    arr1 = radix_sort(arr1)
    print(arr1)
