import numpy as np


class OrderedArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    def printed(self):
        if self.last_position == -1:
            print("The array is empty")
        else:
            for i in range(self.last_position + 1):
                print(i, " - ", self.values[i])

    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print("Maximum capacity reached")
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > value:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1

        self.values[position] = value
        self.last_position += 1

    def search(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] > value:
                return -1
            if self.values[i] == value:
                return i
            if i == self.last_position:
                return -1

    def exclude(self, value):
        position = self.search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[1] = self.values[i + 1]
            self.last_position -= 1


array = OrderedArray(10)
array.printed()

array.insert(6)
array.printed()

array.search(9)
