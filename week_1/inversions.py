def count(t):
    count = 0
    low = 0
    high = 1
    while low < len(t) - 1:
        if t[low] > t[high]:
            count += 1

        if high == len(t) - 1:
            low += 1
            high = low + 1
            continue

        high += 1

    return count

if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12
