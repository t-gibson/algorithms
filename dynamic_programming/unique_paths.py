"""A robot is located at the top-left corner of a m x n grid (marked 'Start'
in the diagram below).
The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).
How many possible unique paths are there?
Example 1:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the
    bottom-right corner:
        1. Right -> Right -> Down
        2. Right -> Down -> Right
        3. Down -> Right -> Right
Example 2:
    Input: m = 7, n = 3
    Output: 28
Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""


def unique_paths(m: int, n: int) -> int:
    """
    Given a robot located at the top-left corner of a m x n grid
    that can only move either down or right at any point in time,
    returns the number of unique paths for the robot to reach the
    bottom-right corner.

    Arguments:
        m (int): Number of rows.
        n (int): Number of columns

    Assumptions:
        1 <= m, n <= 100. So the space, time complexity of an m x n array is bounded
        It's guaranteed that the answer will be <= 2 * 10 ^ 9

    Time complexity: O(n * m)
    Space complexity: O(n * m)
    """
    dp = [[0] * n for _ in range(m)]

    # recurrence
    for i in range(m):
        for j in range(n):
            # base case:
            # along all the walls there is only one path to have gotten there
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


if __name__ == "__main__":
    assert unique_paths(1, 2) == 1
    assert unique_paths(3, 2) == 3
    assert unique_paths(7, 3) == 28
    assert unique_paths(3, 3) == 6
