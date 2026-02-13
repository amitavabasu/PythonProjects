"""
Problem

Generate All Possible Expressions That Evaluate To The Given Target Value
Given a string s that consists of digits ("0".."9") and target, a non-negative integer, find all expressions that can be built from string s that evaluate to the target.

When building expressions, you have to insert one of the following operators between each pair of consecutive characters in s: join or * or +. For example, by inserting different operators between the two characters of string "12" we can get either 12 (1 joined with 2 or "12") or 2 ("1*2") or 3 ("1+2").

Other operators such as - or ÷ are NOT supported.

Expressions that evaluate to the target but only utilize a part of s do not count: entire s has to be consumed.

Precedence of the operators is conventional: join has the highest precedence, * – medium and + has the lowest precedence. For example, 1 + 2 * 34 = (1 + (2 * (34))) = 1 + 68 = 69.

You have to return ALL expressions that can be built from string s and evaluate to the target.

Example
{
"s": "202",
"target": 4
}
Output:

["2+0+2", "2+02", "2*02"]
Same three strings in any other order are also a correct output.

Notes
Order of strings in the output does not matter.
If there are no expressions that evaluate to target, return an empty list.
Returned strings must not contain spaces or any characters other than "0",..., "9", "*", "+".
All returned strings must start and end with a digit.
Constraints:

1 <= length of s <= 13
1 <= target <= 1013
"""
import copy
import re
def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    result = []
    #generate_all_expressions_rec(s, 0, "", target, result)
    def helper(idx, partial_soll):

        # base case
        if idx == len(s):
            fixed_expression = re.sub(r'\b0+(?!\b)', '', partial_soll)
            expression_value = eval(fixed_expression)
            if expression_value == target:
                result.append(copy.deepcopy(partial_soll))
            return
        # recursive-case
        for i in range(idx, len(s)):
            curr = s[idx : i + 1]
            if idx == 0:
                helper(i + 1, partial_soll + curr)
            else:
                helper(i + 1, partial_soll + '+' + curr)
                helper(i + 1, partial_soll + '*' + curr)

    helper(0, "")
    result.append(['-----'])
    generate_all_expressions_rec(s, 0, "", target, result, 0, 0)
    return result

def generate_all_expressions_rec(s, i, partial_soll, target, results, eval_total, prev):
    # backtracking-case
    # base-case
    if i == len(s):
        if eval_total == target:
            results.append(partial_soll)
        return
    else:
    # recursive-case
        curr = s[i]
        curr_int = int(curr)

        generate_all_expressions_rec(s, i + 1, partial_soll + s[i], target, results, (eval_total * 10) + curr_int, curr_int)
        if len(partial_soll) > 0:
            generate_all_expressions_rec(s, i + 1, partial_soll + '+' + s[i], target, results, eval_total + curr_int, curr_int)
            #generate_all_expressions_rec(s, i + 1, partial_soll + '*' + s[i], target, results, (eval_total - prev) + (prev * curr_int), (prev * curr_int))
            generate_all_expressions_rec(s, i + 1, partial_soll + '*' + s[i], target, results,
                                         (eval_total * curr_int), curr_int)




if __name__ == '__main__':
    print(generate_all_expressions("202", 4))
    #print(generate_all_expressions("6666666", 6))
    #print(generate_all_expressions("1234567890123", 1234567890123))