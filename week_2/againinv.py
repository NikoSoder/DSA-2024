def create(n, k):
    elements = create_array(n)
    if k == 0:
        return elements

    ele = elements.pop()
    elements.insert(len(elements) - k, ele)
    return elements


def create_array(n):
    elements = []
    for x in range(1, n + 1):
        elements.append(x)

    return elements


if __name__ == "__main__":
    print(create(3, 0))  # [1,2,3]
    print(create(3, 1))  # esim. [1,3,2]
    print(create(3, 2))  # esim. [3,1,2]
