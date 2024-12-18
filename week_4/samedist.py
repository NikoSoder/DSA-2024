def find(t):
    positions = {}  # element, index
    max_distance = 0
    for idx, num in enumerate(t):
        if num not in positions:
            positions[num] = idx
            continue
        max_distance = max(max_distance, idx - positions[num])

    return max_distance


if __name__ == "__main__":
    print(find([1, 2, 1, 1, 2]))  # 3
    print(find([1, 2, 3, 4]))  # 0
    print(find([1, 1, 1, 1, 1]))  # 4
    print(find([1, 1, 2, 3, 4]))  # 1
    print(find([1, 5, 1, 5, 1]))  # 4
