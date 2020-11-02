"""Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.
Note:
    - The same word in the dictionary may be reused multiple times in the
    segmentation.
    - You may assume the dictionary does not contain duplicate words.
Example 1:
    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet
    code".
Example 2:
    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as
    "apple pen apple".
    Note that you are allowed to reuse a dictionary word.
Example 3:
    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: false
Example 4:
    Input: s = "catsandog", wordDict = ["cats", "sand", "cat", "og"]
    Note: it's not just about matching greedily
"""
from functools import lru_cache
from typing import Tuple


@lru_cache(maxsize=None)
def word_break(s: str, word_dict: Tuple[str]) -> bool:
    """
    Explanation:
        Have gone with the top-down approach with memoization.

    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    n = len(s)
    min_word_length = min(len(word) for word in word_dict)

    # base case
    if n == 0:
        return True
    elif n < min_word_length:
        return False

    # recurrence
    return max(
        word_break(s[len(word):], word_dict)
        for word in word_dict
        if s.startswith(word)
    )


if __name__ == "__main__":
    assert word_break("leetcode", ("leet", "code"))
    assert word_break("applepenapple", ("apple", "pen"))
    assert not word_break("catsandog", ("cats", "dog", "sand", "and", "cat"))

