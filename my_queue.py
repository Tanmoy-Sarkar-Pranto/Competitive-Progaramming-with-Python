class MyQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop(0)
    
    def print_queue(self):
        print(self.items)

    @property
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.size)
    print(q.pop())
    print(q.size)
    print(q.pop())
    print(q.size)