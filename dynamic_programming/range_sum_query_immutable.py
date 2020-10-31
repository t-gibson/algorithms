"""Given an integer array nums, find the sum of the elements between indices i
and j (i ≤ j), inclusive.
Example:
    Given nums = [-2, 0, 3, -5, 2, -1]
    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3
Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.
"""
from typing import Tuple


class Solution:
    """
    Solution:
        To cache computation we store an (n + 1)-array `sums` that holds at index `i`
        the sum of all values of `nums` up to but not including `nums[i]`.
    Time complexity: O(n)
        We initialise the `sums` array once and then all calls to `sum_range()`
        can be completed in constant time.
    Space complexity: O(n)
        For the n-length `sums` array that we store.
    """
    def __init__(self, nums: Tuple[int]) -> None:
        # the base case is the sum is 0
        # this deals with the recurrence below for the case of i == 1
        # were we want the value for sums[1] to be equal to nums[1 - 1]
        self.sums = [0] * (len(nums) + 1)

        # recurrence
        for i in range(1, len(nums) + 1):
            self.sums[i] = self.sums[i - 1] + nums[i - 1]

    def sum_range(self, i: int, j: int) -> int:
        """
        Return the sum of the elements of `nums` between indices `i` and `j`
        (i <= j), inclusive.
        """
        if i > j:
            raise ValueError(f"Left index {i} must be <= right index {j}.")

        return self.sums[j + 1] - self.sums[i]


if __name__ == "__main__":
    nums = (-2, 0, 3, -5, 2, -1)
    s = Solution(nums)
    assert s.sum_range(0, 2) == 1, f"{s.sum_range(0,2)}"
    assert s.sum_range(2, 5) == -1, f"{s.sum_range(2,5)}"
    assert s.sum_range(0, 5) == -3