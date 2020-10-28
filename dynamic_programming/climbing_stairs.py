"""You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
Note: Given n will be a positive integer.
Example 1:
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
Example 2:
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""
from functools import lru_cache

@lru_cache(maxsize=128)
def num_ways(n: int) -> int:
    """
    Top-down solution: Recursion with caching.

    Time complexity: O(n). With the caching. Since for the overlapping
        subproblems we can access their results in constant time.
    Space complexity: O(n). We store values only up to n.
    """
    # base cases
    if n < 1:
        return 1
    elif n == 1:
        return 1

    return num_ways(n - 1) + num_ways(n - 2)

def num_ways_2(n: int) -> int:
    """
    Bottom-up solution: Building an array.

    Complexity is same as above.
    """
    if n < 1:
        return 1
    elif n <= 2:
        return n

    dp = [None] * n

    # base case
    dp[0] = 1 # 1 stair
    dp[1] = 2 # 2 stairs

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]


if __name__ == "__main__":
    assert num_ways(2) == num_ways_2(2) == 2
    assert num_ways(3) == num_ways_2(3) == 3