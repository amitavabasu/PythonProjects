# Segregate Even And Odd Numbers

"""
This is a two pointer approach problem, infused in sort when to swap numbers.



"""
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def segregate(arr):
    if arr is None or len(arr) < 2: return arr
    n = len(arr)
    i = 0
    j = n-1
    while i < j:
        if arr[i] % 2 == 0:
            i = i + 1
        elif arr[j] % 2 != 0:
            j = j - 1
        else:
            swap(arr, i, j)
            i = i + 1
            j = j - 1
    return arr



if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10,11,0,15,17,16]
    print(array)
    arr1 = segregate(array)
    print(array)