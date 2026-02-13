
import copy
def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    result = []
    letter_case_permutations_rec(s, 0, "", result)
    return result

def letter_case_permutations_rec(s, i, part_soll, result):

    if i == len(s):
        result.append(copy.deepcopy(part_soll))
    else:
        c = s[i]
        if c.isdigit():
            letter_case_permutations_rec(s, i+ 1, part_soll + c, result)
        else:
            if c.isupper():
                letter_case_permutations_rec(s, i + 1, part_soll + c, result)
                letter_case_permutations_rec(s, i + 1, part_soll + c.lower(), result)
            else:
                letter_case_permutations_rec(s, i + 1, part_soll + c.upper(), result)
                letter_case_permutations_rec(s, i + 1, part_soll + c, result)

if __name__ == '__main__':
    print(letter_case_permutations("a1z"))
