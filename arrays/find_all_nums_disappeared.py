"""Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.
Example:
    Input:
    [4,3,2,7,8,2,3,1]
    Output:
    [5,6]
"""
from typing import List


def find_disappeared(nums: List[int]) -> List[int]:
    """
    Explanation:

    We have two ways to encode information: the values in the array,
    and the indices of the array. We iterate through the array,
    and store info about the values at their corresponding index: value - 1.

    We want to store something idempotently (i.e. the action will be the same
    no matter how many times we do it). So we swap the sign of the value found at
    `index` to be negative, if it hasn't yet been swapped.

    The output array is formed by iterating through the array and returning
    the indices of all values that are still positive.

    Time complexity: O(n)
    Space complexity: O(1), not including the O(n) output array.
    """

    for num in nums:
        index = abs(num) - 1

        if nums[index] > 0:
            nums[index] *= -1

    return [i + 1 for i, n in enumerate(nums) if n > 0]



if __name__ == "__main__":
    assert find_disappeared([4,3,2,7,8,2,3,1]) == [5,6]