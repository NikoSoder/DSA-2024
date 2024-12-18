def find(t):
    number_count = {}
    for number in t:
        if number in number_count:
            number_count[number] += 1
            continue
        number_count[number] = 1

    for k, v in number_count.items():
        if v == 1:
            return k


if __name__ == "__main__":
    print(find([2, 1, 3, 2, 3]))  # 1
    print(find([5, 5, 9]))  # 9
    print(find([1, 2, 3, 4, 1, 3, 4]))  # 2
    print(find([8]))  # 8
    print(find([7, 1, 7, 4, 4, 5, 1]))  # 5
