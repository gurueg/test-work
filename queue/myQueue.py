"""
    - положительные моменты практически отсутствуют
    - очень медленно, из-за большого количества промежуточных операций
"""
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        if self.front is None:
            self.front = self._queueElement(value)
            self.rear = self.front
        else:
            new_element = self._queueElement(value)
            self.rear.next = new_element
            self.rear = new_element

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        if self.front == self.rear:
            self.rear = None
        self.front = self.front.next
        return value

    def isEmpty(self):
        return self.front is None

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    class _queueElement:
        def __init__(self, value):
            self.value = value
            self.next = None


if __name__ == "__main__":
    pass