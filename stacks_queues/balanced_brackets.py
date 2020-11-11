"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket
(i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or })
of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched.
For example, {[(])} is not balanced because the contents in between { and } are not balanced.
The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of
parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

- It contains no unmatched brackets.
- The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
- Given  strings of brackets, determine whether each sequence of brackets is balanced.
If a string is balanced, return YES. Otherwise, return NO.

Constraints

- 1 <= n <= 10^3
- 1 <= |s| <= 10^3 where |s| is the length of the sequence
- All characters in the sequences ∈ { {, }, (, ), [, ] }.
"""
from queue import Empty, LifoQueue


def is_matching(left, right) -> bool:
    return (left, right) in [("{", "}"), ("[", "]"), ("(", ")")]


def is_balanced(s: str) -> str:
    left_brackets = LifoQueue()
    for bracket in s:
        if bracket in list("{[("):
            left_brackets.put(bracket)
        else: # must be a right bracket
            try:
                left = left_brackets.get_nowait()
            except Empty:
                # if there is no left brackets to check then trivially fails
                return "NO"
            if is_matching(left, bracket):
                continue
            else:
                return "NO"
    return "YES" if left_brackets.qsize() == 0 else "NO"


if __name__ == "__main__":
    assert is_balanced("}") == "NO"
    assert is_balanced("{[()]}") == "YES"
    assert is_balanced("{[()]}{") == "NO"
    assert is_balanced("{[(])}") == "NO"
    assert is_balanced("{{[[(())]]}}") == "YES"
    assert is_balanced("[]()([{}])[]{}[]") == "YES"
