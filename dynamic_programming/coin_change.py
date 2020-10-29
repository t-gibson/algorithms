"""You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.
Example 1:
    Input: coins = [1, 2, 5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
Example 2:
    Input: coins = [2], amount = 3
    Output: -1
Note:
    You may assume that you have an infinite number of each kind of coin.
"""
from typing import List


def min_change(coins: List[int], amount: int) -> int:
    """
    Given a set of `coins` from different denominations and a total `amount`,
    return the fewest number of coins that are needed to make up that `amount`.

    Assumptions:
        - The length of `coins` is non-zero.
        - All values of `coins` are > 0.

    Returns:
        int: The fewest number of coins that are needed to make up amount.
        If that amount of money cannot be made up by any combination of the coins,
        then -1 is returned.
    """
    # create caching of best values found at each value
    # `inf` is our default value to "always lose" when being used in the `min()` fn below
    dp = [0] + ([float("inf")] * amount)

    for coin in coins:
        # we start at `coin` so that our `[i - coin]` index will never get a negative index
        # we end at `amount + 1` so that we index all the way up to the index == `amount`
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1


if __name__ == "__main__":
    assert min_change([1,2,5], 11) == 3
    assert min_change([2], 3) == -1