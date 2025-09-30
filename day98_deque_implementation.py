# Day 98: Deque (Double-Ended Queue) Implementation

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)
        print(f"Added {item} to the front")

    def add_rear(self, item):
        self.items.append(item)
        print(f"Added {item} to the rear")

    def remove_front(self):
        if self.is_empty():
            print("Deque is empty. Nothing to remove from front.")
            return None
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            print("Deque is empty. Nothing to remove from rear.")
            return None
        return self.items.pop()

    def peek_front(self):
        if self.is_empty():
            print("Deque is empty. Nothing at front.")
            return None
        return self.items[0]

    def peek_rear(self):
        if self.is_empty():
            print("Deque is empty. Nothing at rear.")
            return None
        return self.items[-1]

    def display(self):
        print("Current Deque:", self.items)


if __name__ == "__main__":
    dq = Deque()
    dq.add_rear(10)
    dq.add_rear(20)
    dq.add_front(5)
    dq.display()

    print("Front Peek:", dq.peek_front())
    print("Rear Peek:", dq.peek_rear())

    print("Removed from front:", dq.remove_front())
    print("Removed from rear:", dq.remove_rear())
    dq.display()
