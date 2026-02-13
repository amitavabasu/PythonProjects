"""
find all matching parenthesis

n = 1 --> ()
n = 2 --> ()(), (())
n = 3 --> ()()(), ()(()), (())(), (()()), ((()))
"""
import copy
def find_all_matching_parenthesis(n):
    result = []
    find_all_matching_parenthesis_rec_helper(n, n, "", result)
    return result

def find_all_matching_parenthesis_rec_helper(left, right, partial_sol, result):
    # back-tracking case
    if left > right:
        return
    # base-case
    if left == 0 and right == 0:
        result.append(copy.deepcopy(partial_sol))
        return
    else:
        # recursive-case
        if right > 0:
            find_all_matching_parenthesis_rec_helper(left, right-1, partial_sol + ')', result)
        if left > 0:
            find_all_matching_parenthesis_rec_helper(left-1, right, partial_sol + '(', result)

if __name__ == '__main__':
    print(find_all_matching_parenthesis(3))