"""Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.
Example 1:
    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
Example 2:
    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
Example 3
    Input: [-2, 3, -4]
    Output: 24
"""
from typing import List


def max_product(nums: List[int]) -> int:
    """
    Explanation:
        Negative numbers in the array mean that the locally best maximum can
        swap to be the locally best minimum (and vice versa). If we only
        kept track of the locally best maximum then the optimal substructure
        property does not hold.

        Take for example the case of [-2,3,-4]. The best solution is 24. If we
        only recorded the locally best maximum then this value couldn't have
        been found.

        Therefore, we need to record for each sub-problem, the minimum and the
        maximum value of any contiguous sub-array up to and including index i.

    Time complexity: O(n). We do one pass over the nums array.

    Space complexity: O(n). We store two n-length arrays.
    """
    n = len(nums)

    # trivial case
    if not nums:
        return 0
    elif n == 1:
        return nums[0]

    # initialise dp arrays
    # use default value of 1
    local_min = [1] * n
    local_max = [1] * n

    # base case
    local_min[0] = nums[0]
    local_max[0] = nums[0]

    # recurrence
    for i in range(1, n):
        if nums[i] > 0:
            local_max[i] = max(local_max[i - 1] * nums[i], nums[i])
            local_min[i] = min(local_min[i - 1] * nums[i], nums[i])
        else:
            local_max[i] = max(local_min[i - 1] * nums[i], nums[i])
            local_min[i] = min(local_max[i - 1] * nums[i], nums[i])

    return max(local_max)


if __name__ == "__main__":
    assert max_product([2,3,-2,4]) == 6
    assert max_product([-2,0,-1]) == 0
    assert max_product([-2, 3, -4]) == 24
