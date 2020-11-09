"""Given an array of size n, find the majority element. The majority element
is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always
exist in the array.
Example 1:
    Input: [3,2,3]
    Output: 3
Example 2:
    Input: [2,2,1,1,1,2,2]
    Output: 2
"""
from collections import Counter
from typing import List

"""
likely best way to do it must be O(n)

- iterate over array. adding elements.
- once we've passed the halfwaypoint it is possible that we could stop.

- seems the best way is to run a Counter over the array.
- then return value with largest frequency
"""

def majority_element_1(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    n = len(nums)
    count = Counter(nums)

    for num, tally in count.items():
        if tally > n // 2:
            return num


def majority_element_2(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Explanation: Majority means we need to see it more than
    any other element. Therefore, if we have a `count`, that
    goes up by 1 for each instance of the value, and goes down
    by 1 for each instance of any other value. Any element is a
    viable candidate if its counts remains above 0. If it reaches
    0 then we tag in a new value.

    This may result in false negatives, but we should re-pick the
    true majority value again as a future candidate as we continue
    through the array.
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


if __name__ == "__main__":
    for fn in (majority_element_1, majority_element_2):
        assert fn([3,2,3]) == 3
        assert fn([2,2,1,1,1,2,2]) == 2

