# This is a sample Python script.
import math


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def max_heapify(arr):
    if arr is None: return arr
    n = len(arr)
    if n <= 1:
        return arr
    h = int(math.log2(n))
    upper_tree_max_index = ((2 ** h) - 2)
    for i in range(upper_tree_max_index, -1, -1):
        curr_index = i
        while 0 <= curr_index <= upper_tree_max_index:
            lchildi = 2 * curr_index + 1
            rchildi = 2 * curr_index + 2
            index_to_swap = -1
            if lchildi < n and rchildi < n:
                if arr[lchildi] > arr[rchildi]:
                    index_to_swap = lchildi
                else:
                    index_to_swap = rchildi
            elif lchildi < n:
                index_to_swap = lchildi
            elif rchildi < n:
                index_to_swap = rchildi
            else:
                break
            if arr[index_to_swap] > arr[curr_index]:
                swap(arr, curr_index, index_to_swap)
                curr_index = index_to_swap
            else:
                break
    return arr

def extract_max_for_all(arr):
    if arr is None: return arr
    n = len(arr)
    if n <= 1: return arr
    last = n-1
    h = int(math.log2(n))
    while last > 0:
        swap(arr, last, 0)
        last -= 1
        curr_index = 0
        while 0 <= curr_index <= last:
            l_index = 2* curr_index + 1
            r_index = 2* curr_index + 2
            index_to_swap = -1
            if l_index <= last and r_index <= last:
                if arr[l_index] > arr[r_index]:
                    index_to_swap = l_index
                else:
                    index_to_swap = r_index
            elif l_index <= last:
                index_to_swap = l_index
            elif r_index <= last:
                index_to_swap = r_index
            else:
                break
            if arr[index_to_swap] > arr[curr_index]:
                swap(arr, curr_index, index_to_swap)
                curr_index = index_to_swap
            else:
                break
    return arr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   arr1 = [1,2,3,4,5,6,7,8,9,10,11,0,15,17,16]
   print(arr1)
   arr2 = max_heapify(arr1)
   print(arr2)
   arr3 = extract_max_for_all(arr2)
   print(arr3)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
