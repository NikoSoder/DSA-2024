"""
You are given a list containing n integers. Your task is to pick as many integers from
the list as possible. The first number picked can be any number on the list. Each of the
other numbers must be exactly one larger than the preceding number. How many numbers can you pick?

The time complexity of the algorithm should be O(n \log n).
In a file interval.py, implement the function count that returns the maximum number of integers that can be picked as described.
"""


def count(t):
    sums = []
    t = sorted(set(t))
    sum = 1
    for x in range(1, len(t)):
        element = t[x]
        diff = element - t[x - 1]
        if diff == 1:
            sum += 1
        else:
            sums.append(sum)
            sum = 1

    sums.append(sum)
    return max(sums)


if __name__ == "__main__":
    print(count([15, 14, 9, 7, 10, 8]))  # 4 [7,8,9,10,14,15]
    print(count([14, 15, 16, 15, 13]))  # 4
    print(count([1, 1, 1, 1]))  # 1
    print(count([10, 4, 8]))  # 1
    print(count([7, 6, 1, 8]))  # 3
    print(count([1, 2, 1, 2, 1, 2]))  # 2
    print(count([987654, 12345678, 987653, 999999, 987655]))  # 3
