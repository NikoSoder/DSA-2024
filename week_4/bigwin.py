"""
You are given the price of a stock for n days. Your friend tells you the they bought the
stock on one day and sold the stock at a double the price on another day. How many ways this could have happened?
The time complexity of the algorithm should be O(n).
In a file bigwin.py, implement a function count that returns the number of ways.
"""


def count(t):
    orders = {}
    count = 0

    for num in t:
        if num % 2 == 0 and (num // 2) in orders:
            count += orders[num // 2]

        if num in orders:
            orders[num] += 1
        else:
            orders[num] = 1

    return count


if __name__ == "__main__":
    print(count([1, 2, 3, 4]))  # 2
    print(count([1, 1, 1, 1]))  # 0
    print(count([1, 2, 1, 2, 1, 2]))  # 6
    print(count([5, 1, 3, 4, 1, 6]))  # 1
    print(count([5, 3, 5, 5, 2, 3, 4, 3, 3, 4]))  # 2
    print(count([1, 2, 4, 5, 3, 1]))  # 2
