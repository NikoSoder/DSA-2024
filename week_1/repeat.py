"""
Your task is to find out how long is the shortest string that forms the given string when repeated.
For example, when the input string is abcabcabcabc, the shortest repeating string is abc.

The string consists of the characters a-z and contains at most 100 characters.

In a file repeat.py, implement a function find that returns the length of the shortest repeating string.
"""


def find(s):
    s_len = len(s)
    shortest = None
    for idx in range(1, len(s)):
        repeat_time = s_len // idx

        if s[:idx] * repeat_time == s:
            if not shortest:
                shortest = len(s[:idx])
                continue
            shortest = min(shortest, len(s[:idx]))

    if not shortest:
        return len(s)
    return shortest


# better solution
# def find(s):
#     n = len(s)
#     for i in range(1, n + 1):
#         if n % i == 0 and s[:i] * (n // i) == s:
#             return i

if __name__ == "__main__":
    print(find("aaa"))  # 1
    print(find("abcd"))  # 4
    print(find("abcabcabcabc"))  # 3
    print(find("aybabtuaybabtu"))  # 7
    print(find("abcabca"))  # 7
