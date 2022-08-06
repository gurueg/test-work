# from myBuffer import RingBuffer
from deqBuffer import RingBuffer

def main():
    q = RingBuffer(3)
    q.enqueue(1)
    print q
    q.enqueue(2)
    print q
    q.enqueue(3)
    print q
    q.enqueue(4)
    print q
    q.enqueue(5)
    print q
    q.dequeue()
    print q
    q.dequeue()
    print q
    q.enqueue(6)
    print q


if __name__ == "__main__":
    main()