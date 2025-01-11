"""
You are given data about customers arriving to and departing
from a restaurant in the same way as on the course material.

Your task is to find out what is the longest time that the restaurant
is empty between the departure of a customer and the arrival of another customer.

The time complexity of the algorithm should be O(n log n).

In a file restaurant.py, implement a function find that returns the longest time.
"""


def find(a, d):
    events = []
    for time in a:
        events.append((time, 1))
    for time in d:
        events.append((time, 2))

    events.sort()

    counter = 0
    result = 0
    max_departure = 0
    longest_time_empty = 0

    for event in events:
        if event[1] == 1:
            if counter == 0 and max_departure != 0:
                longest_time_empty = max(longest_time_empty, event[0] - max_departure)
            counter += 1
        if event[1] == 2:
            counter -= 1
            max_departure = max(event[0], max_departure)
        result = max(result, counter)

    return longest_time_empty


if __name__ == "__main__":
    # print(find([arrivals], [departures]))
    print(find([1, 6], [2, 9]))  # 4
    print(find([1, 2, 3], [2, 3, 4]))  # 0
    print(find([1, 4, 6, 8], [5, 5, 9, 9]))  # 1
    print(find([1, 10**9], [2, 10**9 + 1]))  # 999999998
