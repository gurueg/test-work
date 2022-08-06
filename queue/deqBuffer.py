# Быстрее, Понятнее, deque
from collections import deque


class RingBuffer:
    def __init__(self, max_length):
        self.body = deque(maxlen=max_length)

    def enqueue(self, value):
        self.body.append(value)

    def dequeue(self):
        return self.body.pop()

    def __str__(self):
        return str(self.body)

if __name__ == "__main__":
    pass