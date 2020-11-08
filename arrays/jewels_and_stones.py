"""You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.  Each character in S is a type of
stone you have.  You want to know how many of the stones you have are also
jewels.
The letters in J are guaranteed distinct, and all characters in J and S are
letters. Letters are case sensitive, so "a" is considered a different type of
stone from "A".
Example 1:
    Input: J = "aA", S = "aAAbbbb"
    Output: 3
Example 2:
    Input: J = "z", S = "ZZ"
    Output: 0
Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


def num_jewels(J: str, S: str) -> int:
    """
    Time complexity: O(n + m)
    Space complexity: O(n)
    """
    jewels = set(J)

    return sum(stone in jewels for stone in S)


if __name__ == "__main__":
    assert num_jewels("aA", "aAAbbbb") == 3
    assert num_jewels("z", "ZZ") == 0

