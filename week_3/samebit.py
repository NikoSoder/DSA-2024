def count(bits):
    n = len(bits)
    result = 0
    zeros = 0
    ones = 0
    result_ones = 0
    for i in range(n):
        # 0
        if bits[i] == "0" and i == 0:
            zeros += 1
            continue
        if bits[i] == "0":
            result += zeros
            zeros += 1
        # 1
        if bits[i] == "1" and i == 0:
            ones += 1
            continue
        if bits[i] == "1":
            result_ones += ones
            ones += 1
    return result + result_ones


if __name__ == "__main__":
    print(count("0101"))  # 2
    print(count("000000"))  # 15
    print(count("0000000"))  # 21
    print(count("000111"))  # 6
    print(count("00100001101100"))  # 46
