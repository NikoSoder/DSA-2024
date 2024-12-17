def count(s):
    zero_count = 0
    one_count = 0
    for x in s:
        if x == "0":
            zero_count += 1
        if x == "1":
            one_count += 1

    return min(zero_count, one_count)


if __name__ == "__main__":
    print(count("01101"))  # 2
    print(count("1111"))  # 0
    print(count("101111"))  # 1
    print(count("00001111"))  # 4
