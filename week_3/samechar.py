"""
A substring is a contiguous string inside a string. For example, the substrings of the
string abc are a, b, c, ab, bc and abc. Your task is to count how many
substrings have the same character at all positions.

The time complexity of the algorithm should be O(n).

In a file samechar.py, implement a function count that returns the desired count.
"""


def count(s):
    count = 0
    active = s[0]

    for idx in range(1, len(s)):
        char = s[idx]
        if active[0] == char:
            active += char
            continue
        else:
            count += (len(active) * (len(active) + 1)) // 2
            active = ""
            active += char

    count += (len(active) * (len(active) + 1)) // 2
    return count


if __name__ == "__main__":
    print(count("aaa"))  # 6
    print(count("abbbcaa"))  # 11
    print(count("abcde"))  # 5
