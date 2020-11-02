"""Given an integer array with all positive numbers and no duplicates, find
the number of possible combinations that add up to a positive integer target.
Example:
    nums = [1, 2, 3]
    target = 4
    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    Note that different sequences are counted as different combinations.
    Therefore the output is 7.
Follow up:
    What if negative numbers are allowed in the given array?
    How does it change the problem?
    What limitation we need to add to the question to allow negative numbers?
"""
from typing import Tuple
from functools import lru_cache


@lru_cache(maxsize=None)
def combination_sum_top_down(nums: Tuple[int], target: int) -> int:
    """
    Given an integer array `nums` with:
        - all positive numbers
        - no duplicates
        - unsorted
    Returns the number of possible combinations that add up to the positive integer `target`.
    """
    # base case
    if target == 0:
        return 1
    elif target < 0:
        return 0

    # recurrence
    return sum(combination_sum(nums, target - num) for num in nums)


def combination_sum_bottom_up(nums: Tuple[int], target: int) -> int:
    dp = [0] * (target + 1)

    # base case
    dp[0] = 1

    # recurrence
    for i in range(target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]

    return dp[-1]


if __name__ == "__main__":
    for fn in (combination_sum_top_down, combination_sum_bottom_up):
        assert fn((1,2,3), 4) == 7
        assert fn((1,2,3,4), 6) == 29
