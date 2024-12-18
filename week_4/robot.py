def count(s):
    position = (0, 0)  # x, y
    directions = {(0, 0): 1}

    for letter in s:
        if letter == "U":
            position = (position[0], position[1] - 1)
            if position not in directions:
                directions[position] = 1
        if letter == "D":
            position = (position[0], position[1] + 1)
            if position not in directions:
                directions[position] = 1
        if letter == "L":
            position = (position[0] - 1, position[1])
            if position not in directions:
                directions[position] = 1
        if letter == "R":
            position = (position[0] + 1, position[1])
            if position not in directions:
                directions[position] = 1
    return len(directions)


if __name__ == "__main__":
    print(count("LL"))  # 3
    print(count("UUDLRR"))  # 5
    print(count("UDUDUDU"))  # 2
