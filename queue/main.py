from arrayQueue import Queue

def main():
    q = Queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)

    print q.peek()
    while(not q.isEmpty()):
        print q.dequeue()

    print q.isEmpty


if __name__ == "__main__":
    main()