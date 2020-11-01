"""Given an unsorted array of integers, find the length of longest increasing
subsequence.
Example:
        Input: [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101],
        therefore the length is 4.
Note:
    - There may be more than one LIS combination, it is only necessary for you
    to return the length.
    - Your algorithm should run in O(n ^ 2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from typing import List


def length_of_lis(nums: List[int]) -> int:
    # trivial case
    if not nums:
        return 0
    elif len(nums) == 1:
        return 1

    n = len(nums)

    # dp matrix
    # caches the results for the LIS for the array up to and including index i
    # default value is 1. since theres the 1-length subsequence as a backup
    dp = [1] * n

    for end in range(1, n):
        for start in range(end):
            if nums[start] < nums[end]:
                # the longest LIS can be updated as either what it has currently,
                # or the longest LIS found at index `start` + 1
                dp[end] = max(dp[end], dp[start] + 1)
                # we continuously update dp[end] for all considered values of `start`

    return dp[-1]


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    assert length_of_lis(nums) == 4