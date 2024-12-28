"""
You are given a list consisting of n integers. n-1 of the integers are equal
and one has a different value. Your task is to determine what the different integer is.
The time complexity of the algorithm should be O(n). You may assume that n>2.
In a file onlyone.py, implement a function find that returns the desired integer.
"""


# 0.06s with 1mil numbers
def find(t):
    m = {}
    for num in t:
        if num in m:
            m[num] += 1
        else:
            m[num] = 1

    for key, value in m.items():
        if value == 1:
            return key


# NOTE: faster solutions
# 0.01s with 1mil numbers

# def find(t):
#     number1 = min(t)
#     number2 = max(t)
#     if t.count(number1) == 1:
#         return number1
#     else:
#         return number2

# def find(t):
#     other = None
#     for x in t:
#         if x == other:
#             continue
#         if t.count(x) == 1:
#             return x
#         other = x

if __name__ == "__main__":
    print(find([1, 1, 2, 1]))  # 2
    print(find([4, 5, 5]))  # 4
    print(find([1, 1, 1, 1, 2]))  # 2
    print(find([8, 8, 5, 8, 8]))  # 5
