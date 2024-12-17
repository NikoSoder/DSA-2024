def count(t):
    total = 0
    for element in t:
        if isinstance(element, int):
            print("hello world")
            total += 1
        elif isinstance(element, list):
            total += count(element)

    return total


if __name__ == "__main__":
    print(count([1, 2, 3]))  # 3
    print(count([1, [2, 3], 4, 5, [6]]))  # 6
    print(count([1, [1, [1, [1]]]]))  # 4
    print(count([[1, 2, [3, 4]], 5, [[6, [7], 8]]]))  # 8
