"""Say you have an array for which the ith element is the price of a given
stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.
Note that you cannot sell a stock before you buy one.
Example 1:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
                 profit = 6-1 = 5.
                 Not 7-1 = 6, as selling price needs to be larger than buying
                 price.
Example 2:
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
from typing import List


def buy_sell(arr: List[int]) -> int:
    """
    Solution:
    We traverse the array and keep a record of the index of the highest
    and lowest value.

    The curveball being that if we encounter a new lowest value, we need to
    reset our highest value as well. This is because we must buy before we can
    sell. Therefore, their is a constraint that `index_low <= index_high`.

    Time complexity: O(n). We do a single pass over the array.
    Space complexity: O(1). We are only storing in runtime the indices of low
        and high.
    """
    index_lowest = 0
    index_highest = 0

    for i in range(len(arr)):
        if arr[index_lowest] > arr[i]:
            index_lowest = i
            index_highest = i
        elif arr[index_highest] < arr[i]:
            index_highest = i

    return arr[index_highest] - arr[index_lowest]


if __name__ == "__main__":
    assert buy_sell([7,6,4,3,1,5]) == 4
    assert buy_sell([7,6,4,3,1]) == 0
    assert buy_sell([7,1,5,3,6,4]) == 5