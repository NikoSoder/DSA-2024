"""
Implement the class FastMode with the following methods:

add(x, k): add the number x to the list k times

mode(): return the mode of the list, i.e., the most frequent element 
(if there are multiple modes, return the smallest of them)

The time complexity of both methods should be O(1).
In a file fastmode.py, implement a class 
FastMode according to the following template:
"""


class FastMode:
    def __init__(self):
        self.hash = {}
        self.biggest = 0
        self.key = 0

    def add(self, x, k):
        if x in self.hash:
            self.hash[x] += k
            if self.hash[x] > self.biggest:
                self.biggest = self.hash[x]
                self.key = x
            if self.hash[x] == self.biggest:
                self.biggest = self.hash[x]
                smaller = min(x, self.key)
                self.key = smaller
            return
        self.hash[x] = k
        if k > self.biggest:
            self.biggest = k
            self.key = x
        if k == self.biggest:
            smaller = min(x, self.key)
            self.key = smaller

    def mode(self):
        return self.key


if __name__ == "__main__":
    m = FastMode()
    m.add(4, 7)
    print(m.mode())  # 4
    m.add(8, 5)
    print(m.mode())  # 4
    m.add(8, 3)
    print(m.mode())  # 8
    m.add(4, 1)
    print(m.mode())  # 4
