"""
Your task is to implement the class NearList that is given a list of numbers in the constructor.

The class should have an efficient method find(x) that finds the list number that is
nearest to the number x by value. If the answer is not unique, the method should return the smaller number.

You may assume that all the numbers in the task are integers.
In a file nearlist.py, implement a class NearList according to the following template:
"""


class NearList:
    def __init__(self, t):
        self.nlist = sorted(t)

    def find(self, x):
        if x > self.nlist[-1]:
            return self.nlist[-1]

        low = 0
        high = len(self.nlist) - 1
        while low <= high:
            mid = (low + high) // 2

            if self.nlist[mid] > x:
                high = mid - 1
            elif self.nlist[mid] < x:
                low = mid + 1
            else:
                return x

        low_diff = abs(x - self.nlist[low])
        high_diff = abs(x - self.nlist[high])
        if low_diff == high_diff:
            return min(self.nlist[low], self.nlist[high])
        elif high_diff > low_diff:
            return self.nlist[low]
        else:
            return self.nlist[high]


if __name__ == "__main__":
    n = NearList([3, 6, 1, 3, 9, 8])
    print(n.find(1))  # 1
    print(n.find(2))  # 1
    print(n.find(3))  # 3
    print(n.find(4))  # 3
    print(n.find(5))  # 6
    print(n.find(6))  # 6
    print(n.find(7))  # 6
    print(n.find(8))  # 8
    print(n.find(9))  # 9
