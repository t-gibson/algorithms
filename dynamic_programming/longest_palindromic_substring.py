"""Given a string s, find the longest palindromic substring in s. You may
assume that the maximum length of s is 1000.
Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
Example 2:
    Input: "cbbd"
    Output: "bb"
"""
from typing import List


def longest_palindrome(s: str) -> str:
    """
    Constraints:
        - 1 <= s.length <= 1000
        - s consist of only digits and English letters (lower-case and/or upper-case)

    Time complexity: O(n^2). We iterate over the (n x n) dp matrix
    Space compelxity: O(n^2). We store the (n x n) dp matrix.
    """
    min_start = max_end = 0

    n = len(s)

    # dp array that stores the boolean value of whether a palindrome is found for start = i, end = j
    dp = [[False] * n for _ in range(n)]

    # recurrence
    for end in range(n):
        for start in range(end, -1, -1):
            # if start = end, then automatically a 1-length palindrome
            if start == end:
                dp[start][end] = True
            # if substring length is 2, then palindrom if s[start] == s[end]
            elif end - start == 1:
                dp[start][end] = (s[start] == s[end])
            # else, a palindrome if the ends match and dp[start + 1][end - 1] is True
            else:
                dp[start][end] = (s[start] == s[end]) and dp[start + 1][end - 1]

            # if was a palindromic substring and is maximal, then keep a record
            if dp[start][end] and max_end - min_start < end - start:
                max_end = end
                min_start = start
                print(s[min_start:max_end + 1])

    # we slice up to max_end + 1 as an artefact of python slicing
    return s[min_start:max_end + 1]


if __name__ == "__main__":
    assert longest_palindrome("babad") in ["bab","aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("ac") in ["a", "c"]
    assert longest_palindrome("abbdebba") == "bb"