import copy
def find_all_arrangements(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_str
    """

    ps = [i for i in range(0, n)]
    result = []
    helper( 0, ps, result)
    final_result = []
    for i in range(len(result)):
        res_list = []
        for j in range(n):
            string_list = ['-' for _ in range(n)]
            item = result[i][j]
            string_list[item] = 'q'
            res_list.append("".join(string_list))
        final_result.append(res_list)
    return final_result


def helper(i, ps, result):
    if not is_valid(ps, i): return
    if i == len(ps):
        result.append(copy.deepcopy(ps))
        return
    for j in range(i, len(ps)):
        ps[i], ps[j] = ps[j], ps[i]
        helper(i+1, ps, result)
        ps[i], ps[j] = ps[j], ps[i]

def is_valid(ps, i):
    c_row = i - 1
    c_col = ps[i - 1]
    for j in range(0, i-1):
        row = j
        col = ps[j]
        if abs(c_row - row) == abs(c_col - col):
            return False
    return True

if __name__ == '__main__':
    print(find_all_arrangements(4))
