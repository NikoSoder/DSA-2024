def solve(t, x):
    boxes = sorted(t)
    boxes_sum = 0
    if x < boxes[0]:
        return boxes_sum

    for box in boxes:
        if x == 0:
            break
        if x >= box:
            boxes_sum += 1
            x -= box
        else:
            return boxes_sum

    return boxes_sum


if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2))  # 2
    print(solve([2, 5, 3, 2, 8, 7], 10))  # 3
    print(solve([2, 3, 4, 5], 1))  # 0
    print(solve([2, 3, 4, 5], 10**9))  # 4
    print(solve([10**9, 1, 10**9], 10**6))  # 1
