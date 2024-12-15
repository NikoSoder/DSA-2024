import math

def count(a, b, c):
    first_count = c / a
    second_count = c / b
    return math.floor(max(first_count, second_count))


if __name__ == "__main__":
    print(count(3, 4, 11))  # 3
    print(count(5, 1, 100))  # 100
    print(count(2, 3, 1))  # 0
    print(count(2, 3, 9))  # 4
