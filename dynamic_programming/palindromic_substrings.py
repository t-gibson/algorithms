"""Given a string, your task is to count how many palindromic substrings in
this string.
The substrings with different start indexes or end indexes are counted as
different substrings even they consist of same characters.
Example 1:
    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""
from typing import List, Tuple


def count_substrings(s: str) -> int:
    """
    Given a string `s`, returns the count of palindromic substrings in this
    string.
    The substrings with different start or end indices are counted as different
    substrings even if they consist of the same characters.

    Time complexity: O(n ^ 2)
    Space complexity: O(n^2). The n x n dp matrix.
    """
    n = len(s)

    # trivial case
    if not s:
        return 0
    elif n == 1:
        return 1

     # dp array and substring store
    dp = [[False] * n for _ in range(n)]
    substrings = 0

    # recurrence
    for end in range(n):
        for start in range(end, -1, -1):
            if start == end:
                dp[start][end] = True
            elif end - start == 1:
                dp[start][end] = s[start] == s[end]
            else:
                dp[start][end] = (s[start] == s[end]) and dp[start + 1][end - 1]

            if dp[start][end]:
                substrings += 1

    return substrings


if __name__ == "__main__":
    assert count_substrings("abc") == 3
    assert count_substrings("aaa") == 6