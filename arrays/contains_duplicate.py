"""Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.
Example 1:
    Input: [1,2,3,1]
    Output: true
Example 2:
    Input: [1,2,3,4]
    Output: false
Example 3:
    Input: [1,1,1,3,3,4,3,2,4,2]
    Output: true
"""
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    existing_nums = set()
    for num in nums:
        if num in existing_nums:
            return True
        else:
            existing_nums.add(num)

    return False


if __name__ == "__main__":
    assert contains_duplicate([1,2,3,1])
    assert not contains_duplicate([1,2,3,4])
    assert contains_duplicate([1,1,1,3,3,4,3,2,4,2])
