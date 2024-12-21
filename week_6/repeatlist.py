"""
Implement the class RepeatList with the following methods:

add(x): add the number x to the list
check(): return True if some number repeats on the list, otherwise False

The time complexity of each method should be O(1).
In a file repeatlist.py, implement a class RepeatList according to the following template:
"""


class RepeatList:
    def __init__(self):
        self.hash = {}
        self.has_dub = False

    def add(self, x):
        if x not in self.hash:
            self.hash[x] = 1
            return
        self.hash[x] += 1
        self.has_dub = True

    def check(self):
        return self.has_dub


if __name__ == "__main__":
    r = RepeatList()
    print(r.check())  # False
    r.add(1)
    r.add(2)
    r.add(3)
    print(r.check())  # False
    r.add(2)
    print(r.check())  # True
    r.add(5)
    print(r.check())  # True
