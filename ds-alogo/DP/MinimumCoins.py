"""
Problem

Minimum Coins
Given a variety of coin types defining a currency system, find the minimum number of coins required to express a given amount of money. Assume infinite supply of coins of every type.

Example
{
"coins": [1, 3, 5],
"value": 9
}
Output:

3
Here are all the unique ways to express 9 as a sum of coins 1, 3 and 5:

1, 1, 1, 1, 1, 1, 1, 1, 1
1, 1, 1, 1, 1, 1, 3
1, 1, 1, 1, 5
1, 1, 1, 3, 3
1, 3, 5
3, 3, 3
Last two ways use the minimal number of coins, 3.

Notes
There will be no duplicate coin types in the input.

Constraints:

1 <= number of coin types <= 102
1 <= coin value <= 102
1 <= amount of money to express <= 104
"""

import math
def minimum_coins(coins, value):
    """
    Args:
     coins(list_int32)
     value(int32)
    Returns:
     int32
    """
    n = len(coins)
    if n == 0 or value <= 0: return 0
    table = [math.inf] * (value + 1)
    table[0] = 0
    for i in range(1, value + 1):
        for j in range(n):
            if i - coins[j] >= 0:
                table[i] = min(table[i - coins[j]], table[i])
        table[i] += 1
    if table[value] == math.inf:
        return -1
    else:
        return table[value]

if __name__ == "__main__":
    print(minimum_coins([1, 3, 5], 12))