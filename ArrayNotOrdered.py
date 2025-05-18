import numpy as np

class ArrayNotOrditaned:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    def printed(self):
        if self.last_position == -1:
            print("The array is empty")
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])

array = ArrayNotOrditaned(5)
array.printed()