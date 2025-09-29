# Day 96: Queue Implementation (Enqueue, Dequeue, Peek)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        return self.items[0]

    def display(self):
        print("Current Queue:", self.items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()

    print("Peek:", queue.peek())
    print("Dequeue:", queue.dequeue())
    queue.display()
