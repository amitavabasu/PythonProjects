import copy
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    results = []
    get_permutations_rec(arr, 0, results);
    return results

def get_permutations_rec(arr, i, results):
    # base-case
    if i == len(arr):
        results.append(copy.deepcopy(arr))
        return
    else:
    # recursive-case
        for j in range(i, len(arr)):
            arr[j], arr[i] = arr[i], arr[j]
            get_permutations_rec(arr, i+1, results)
            arr[j], arr[i] = arr[i], arr[j]

if __name__ == "__main__":
    arr = [1, 2, 2]
    print(get_permutations(arr))