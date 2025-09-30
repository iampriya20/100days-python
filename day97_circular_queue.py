# Day 97: Circular Queue Implementation

class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_full(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self) -> bool:
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
            return None
        removed_item = self.queue[self.front]
        if self.front == self.rear:
            # Queue becomes empty
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return removed_item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Current Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()


if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.display()

    print("Peek:", cq.peek())
    print("Dequeue:", cq.dequeue())
    cq.display()
