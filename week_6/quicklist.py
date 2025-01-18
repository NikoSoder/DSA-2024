"""
Implement a class QuickList with the following methods:

move(k): move the first k elements of the list to the end of the list
get(i): return the element at the index i

The initial contents of the list is given as a parameter to the constructor. The time complexity of both methods should be O(1).
In a file quicklist.py, implement a class QuickList according to the following template:
"""


class QuickList:
    def __init__(self, t):
        self.quick_list = t
        self.offset = 0

    def move(self, k):
        self.offset = (self.offset + k) % len(self.quick_list)

    def get(self, i):
        real_index = (self.offset + i) % len(self.quick_list)
        return self.quick_list[real_index]


if __name__ == "__main__":
    q = QuickList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(q.get(4))  # 5
    q.move(3)
    print(q.get(4))  # 8
    q.move(3)
    print(q.get(4))  # 1
    q.move(10)
    print(q.get(4))  # 1
    q.move(7)
    q.move(5)
    print(q.get(0))  # 9
