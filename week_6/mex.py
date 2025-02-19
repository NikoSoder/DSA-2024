"""
Implement a class Mex with the following method:

add(x): add the number x to the list and return the mex number of the list

The mex number of a list is the smallest non-negative integer that does not
occur on the list. For example, the mex number of the list [2,0,3,4,2] is 1.
The method add should take O(1) time on average. You may assume that all
the numbers added to the list are non-negative.

In a file mex.py, implement a class Mex according to the following template:
"""


class Mex:
    def __init__(self):
        self.nums = set()
        self.mex = 0

    def add(self, x):
        self.nums.add(x)
        if x == self.mex:
            biggest = self.mex
            for idx in range(self.mex, len(self.nums)):
                if idx > biggest:
                    biggest = idx
                if idx not in self.nums:
                    self.mex = idx
                    break
                if idx == len(self.nums) - 1:
                    pass
                    self.mex = biggest + 1
        return self.mex


if __name__ == "__main__":
    m = Mex()
    print(m.add(1))  # 0
    print(m.add(3))  # 0
    print(m.add(4))  # 0
    print(m.add(0))  # 2
    print(m.add(5))  # 2
    print(m.add(2))  # 6
