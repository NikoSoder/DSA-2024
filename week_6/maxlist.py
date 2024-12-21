"""
Implement a class MaxList with the following methods:

add(x): add the number x to the list
max(): return the largest number on the list (or None if the list is empty)

The time complexity of both methods should be O(1).
In a file maxlist.py, implement a class MaxList according to the following template:
"""


class MaxList:
    def __init__(self):
        self.stack = []
        self.max_value = None

    def add(self, x):
        self.stack.append(x)
        if self.max_value is None or x > self.max_value:
            self.max_value = x

    def max(self):
        return self.max_value


if __name__ == "__main__":
    m = MaxList()
    print(m.max())  # None
    m.add(1)
    m.add(2)
    m.add(3)
    print(m.max())  # 3
    m.add(8)
    m.add(5)
    print(m.max())  # 8
