

import copy
def get_distinct_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    #result = set()
    result = []
    s = "".join(sorted(s))
    #get_distinct_subsets_rec(s, 0, "", result)
    get_distinct_subsets_rec2(s, 0, "", result)
    return result



# def get_distinct_subsets_rec(s, i, ps, result):
#     #base-case
#     if i == len(s):
#         if ps not in result:
#             result.add(ps)
#         return
#     else:
#         get_distinct_subsets_rec(s, i + 1, ps + s[i], result)
#         get_distinct_subsets_rec(s, i+1, ps, result)


def get_distinct_subsets_rec2(s, i, ps, result):
    #base-case
    if i == len(s):
        result.append(ps)
        return
    j = i + 1
    while j < len(s) and s[i] == s[j]:
        j += 1
    count = 0
    include = ""
    get_distinct_subsets_rec2(s, j, ps + include, result)
    while count < j - i:
        include += s[i]
        get_distinct_subsets_rec2(s, j, ps + include, result)
        count += 1

if __name__ == "__main__":
    str = "dc"
    print(get_distinct_subsets(str))