"""Given an array of integer nums containing n + 1 integers where each integer is between
1 and n (inclusive), prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.
Example 1:
    Input: [1,3,4,2,2]
    Output: 2
Example 2:
    Input: [3,1,3,4,2]
    Output: 3
Note:
    - You must not modify the nums (assume the nums is read only).
    - You must use only constant, O(1) extra space.
    - Your runtime complexity should be less than O(n^2).
    - There is only one duplicate number in the nums, but it could be repeated
    more than once.
"""
from typing import List

"""
guaranteed to be only one by the pigeonhole principle
how could we encode info from the whole array, into O(1)


we can sum up the array and find the difference with 1 + ... n
"""

def find_duplicate(nums: List[int]) -> int:
    """
    Explanation:
    Given that there is exactly one extra, then we can find the value as
    the difference between the actual sum of the array and the sum of
    1 + 2 + .. + n.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    n = len(nums) - 1
    total_sum = sum(range(1, n + 1))
    actual_sum = sum(nums)

    return actual_sum - total_sum


if __name__ == "__main__":
    x = [1, 3, 4, 2, 2]
    assert find_duplicate(x) == 2

    y = [3, 1, 3, 4, 2]
    assert find_duplicate(y) == 3