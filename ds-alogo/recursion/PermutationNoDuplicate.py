
import copy
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    result = []
    get_permutations_rec(arr, 0, result)
    return result

def get_permutations_rec(arr, i, result):
    dup = set()
    if i == len(arr):
        result.append(copy.deepcopy(arr))
        return
    else:
        for j in range(i, len(arr)):
            arr[j], arr[i] = arr[i], arr[j]
            if arr[i] not in dup:
                dup.add(arr[i])
                get_permutations_rec(arr, i+ 1, result)
            arr[j], arr[i] = arr[i], arr[j]


if __name__ == "__main__":
    arr = [1, 2, 2]
    print(get_permutations(arr))
