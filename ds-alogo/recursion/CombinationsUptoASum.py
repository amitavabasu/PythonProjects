import copy
def generate_all_combinations(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    result = []
    arr.sort()
    helper(arr, 0, target, [], result)
    return result


def helper(arr, i, target, ps, result):
    if  target == 0:
        result.append(copy.deepcopy(ps))
        return
    if i == len(arr) or target < 0 :
        return
    else:
        j = i
        while j < len(arr) and arr[i] == arr[j]:
            j += 1

        helper(arr, j, target, ps, result)

        count = 1
        while count <= j - i:
            ps.append(arr[i])
            helper(arr, j, target - count * arr[i], ps, result)
            count += 1
        count = 1
        while count <= j - i:
            ps.pop()
            count += 1

if __name__ == '__main__':
    print(generate_all_combinations([1, 1, 1, 1], 2))
    print(generate_all_combinations([1, 2, 3], 3))
    print(generate_all_combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 300))
