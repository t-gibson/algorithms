"""Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.
Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
    If you have figured out the O(n) solution, try coding another solution
    using the divide and conquer approach, which is more subtle.
"""
from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    Given an integer array `nums`, the contiguous subarray (containing at least
    one number) which has the largest sum is found, and its sum is returned.
    """
    n = len(nums)

    # trivial case
    if not nums:
        raise ValueError(f"Integer array is empty")
    elif n < 2:
        return nums[0]

    # dp array that will hold the best decision to be made at each i-th position
    dp = [-float("inf")] * n

    # base case
    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    return max(dp)


if __name__ == "__main__":
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6