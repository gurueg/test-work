# Положительных черт не назову
# Сложнее в реализации
# Сложнее в понимании
# Медленнее в исполнении
class RingBuffer:
    def __init__(self, max_length):
        self.front = None
        self.rear = None
        self.max_length = max_length
        self.elements_count = 0
    
    def enqueue(self, value):
        new_element = self._queueElement(value)
        if self.front is None:
            self.front = new_element
            self.front.right = self.front
            self.front.left = self.front
            self.rear = self.front
            self.elements_count += 1
        else:
            self.rear.right = new_element
            if self.elements_count == self.max_length:
                self.front = self.front.right
                self.front.left = new_element
            else:
                self.elements_count += 1
            new_element.right = self.front
            new_element.left = self.rear
            self.rear = new_element

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        left = self.front.left
        right = self.front.right

        right.left, left.right = left, right
        self.front = right
        self.elements_count -= 1
        return value
    
    def __str__(self):
        result = []
        element = self.front
        for i in range(self.elements_count):
            result.append(element.value)
            element = element.right
        return str(result)

    class _queueElement:
        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

        def __str__(self):
            return str(self.right)


if __name__ == "__main__":
    pass