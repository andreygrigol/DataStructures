import numpy as np


class ArrayNotOrditaned:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # O(n)
    def printed(self):
        if self.last_position == -1:
            print("The array is empty")
        else:
            for i in range(self.last_position + 1):
                print(i, " - ", self.values[i])

    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print("Maximum capacity reached")
        else:
            self.last_position += 1
            self.values[self.last_position] = value


array = ArrayNotOrditaned(5)
array.printed()
