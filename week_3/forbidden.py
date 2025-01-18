"""
Your task is to count how many substrings of a string do not contain the character a.

The time complexity of the algorithm should be O(n).

In a file forbidden.py, implement a function count that returns the desired count.
"""


def count(s):
    count = 0
    result = 0

    for idx in range(len(s)):
        if s[idx] == "a":
            count = 0
        else:
            count += 1
        result += count

    return result


if __name__ == "__main__":
    print(count("aaa"))  # 0
    print(count("saippuakauppias"))  # 23
    print(count("x"))  # 1
    print(count("aybabtu"))  # 9
