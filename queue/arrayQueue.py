"""
 + просто
 + быстро
"""
class Queue:
    def __init__(self):
        self.body = []

    def enqueue(self, value):
        self.body.append(value)

    def dequeue(self):
        if len(self.body) < 1:
            return None
        return self.body.pop(0)

    def isEmpty(self):
        return len(self.body) < 1

    def peek(self):
        if  len(self.body) < 1:
            return None
        return self.body[0]


if __name__ == "__main__":
    pass