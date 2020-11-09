"""Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
Example:
    Input:
    [4,3,2,7,8,2,3,1]
    Output:
    [2,3]
"""
from typing import List


def find_duplicates(nums: List[int]) -> List[int]:
    dupes = []

    for num in nums:
        index = abs(num) - 1

        if nums[index] > 0:
            nums[index] *= -1
        else:
            dupes.append(abs(num))

    return dupes


if __name__ == "__main__":
    assert find_duplicates([4,3,2,7,8,2,3,1]) == [2,3]
    assert find_duplicates([1, 2, 3, 3, 5, 6, 6, 8]) == [3,6]
