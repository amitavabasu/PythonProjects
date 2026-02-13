"""
Problem

Palindromic Decomposition Of A String
Find all palindromic decompositions of a given string s.

A palindromic decomposition of string is a decomposition of the string into substrings, such that all those substrings are valid palindromes.

Example
{
"s": "abracadabra"
}
Output:

["a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a", "a|b|r|a|c|a|d|a|b|r|a"]
Notes
Any string is its own substring.
Output should include ALL possible palindromic decompositions of the given string.
Order of decompositions in the output does not matter.
To separate substrings in the decomposed string, use | as a separator.
Order of characters in a decomposition must remain the same as in the given string. For example, for s = "ab", return ["a|b"] and not ["b|a"].
Strings in the output must not contain whitespace. For example, ["a |b"] or ["a| b"] is incorrect.
Constraints:

1 <= length of s <= 20
s only contains lowercase English letters.
"""

def is_palindrome(s):
    if len(s) == 0: return False
    if len(s) == 1: return True
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def generate_palindromic_decompositions_rec(s, i, partial_sol, last_string, results):
    if i == len(s):
        if is_palindrome(last_string):
            results.append(partial_sol)
        return
    else:
        generate_palindromic_decompositions_rec(s, i + 1, partial_sol + s[i], last_string + s[i], results)
        if is_palindrome(last_string):
            generate_palindromic_decompositions_rec(s, i + 1, partial_sol + '|' + s[i], s[i], results)
        else:
            return

def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    partial_sol = ""
    soll_collector = ""
    results = []
    generate_palindromic_decompositions_rec(s, 0, partial_sol, soll_collector, results)
    return results


if __name__ == '__main__':
    print(generate_palindromic_decompositions("abracadabra"))
