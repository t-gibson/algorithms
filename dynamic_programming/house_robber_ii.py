"""You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed. All houses at this place are
arranged in a circle. That means the first house is the neighbor of the last
one. Meanwhile, adjacent houses have security system connected and it will
automatically contact the police if two adjacent houses were broken into on
the same night.
Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
Example 1:
    Input: [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3
    (money = 2), because they are adjacent houses.
Example 2:
    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.
"""
from typing import List


class Solution:
    """
    Assumptions:
        - houses[i] >= 0 for all i

    Explanation:
        The solution is a minor adjustment of the previous one. We find the
        maxmimum money returned from either considering robbing all houses
        bar the first one, or bar the last one.

    Time complexity: O(n). Each call to the `_rob()` helper method is O(n) and
        we call it twice at each call to `max_money()`

    Space complexity: O(n). We store a copy of the n-length `houses` array.
    """
    def max_money(self, houses: List[int]) -> int:
        n = len(houses)
        # deal with trivial cases:
        if n == 0:
            return 0
        elif n <= 2:
            return max(houses)

        return max(self._rob(houses[1:]), self._rob(houses[:-1]))

    @staticmethod
    def _rob(houses: List[int]) -> int:
        n = len(houses)

        dp = [-float("inf")] * n

        # base cases
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])

        # recurrence
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.max_money([2,3,2]) == 3
    assert s.max_money([1,2,3,1]) == 4
    assert s.max_money([3,2,5,2,7]) == 12