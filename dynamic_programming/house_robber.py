"""You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping you
from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
Example 1:
    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.
Example 2:
    Input: [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob
    house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.
"""
from typing import List


def max_money(houses: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        houses (array, int): A list of non-negative integers representing the
            amount of money of each house.
    """
    n = len(houses)

    # deal with trivial cases:
    if n == 0:
        return 0
    elif n <= 2:
        return max(houses)

    dp = [-float("inf")] * n

    # base cases
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    # recurrence
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])

    return dp[-1]


if __name__ == "__main__":
    assert max_money([1,2,3,1]) == 4
    assert max_money([2,7,9,3,1]) == 12