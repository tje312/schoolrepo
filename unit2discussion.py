"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # Internal list to store stack items
        self.items = []

    def push(self, value):
        # Add value to the top of the stack (LIFO)
        self.items.append(value)

    def pop(self):
        # Remove and return the most recently added value
        if self.is_empty():
            return "Stack is empty. Nothing to remove."
        return self.items.pop()

    def peek(self):
        # Return the top value without removing it
        if self.is_empty():
            return "Stack is empty. Nothing to peek at."
        return self.items[-1]

    def is_empty(self):
        # True if the stack has no values
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # Use deque for efficient FIFO operations
        self.items = deque()

    def enqueue(self, value):
        # Add value to the back of the queue
        self.items.append(value)

    def dequeue(self):
        # Remove and return the value from the front
        if self.is_empty():
            return "Queue is empty. Nothing to remove."
        return self.items.popleft()

    def front(self):
        # Return the front value without removing it
        if self.is_empty():
            return "Queue is empty. Nothing at the front."
        return self.items[0]

    def is_empty(self):
        # True if the queue has no values
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")
    stack = Stack()

    print("Adding items to the stack:")
    for value in [10, 20, 30, 40]:
        stack.push(value)
        print(f"Pushed: {value}")

    print(f"\nTop item using peek(): {stack.peek()}")

    print("\nRemoving items (LIFO - Last In, First Out):")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")

    print("\nTesting pop() on an empty stack:")
    print(stack.pop())

    print("\nTesting peek() on an empty stack:")
    print(stack.peek())

    print("\nTesting a single-item stack:")
    single_stack = Stack()
    single_stack.push(100)
    print("Added item: 100")
    print(f"Removed item: {single_stack.pop()}")
    print(f"Is the stack empty? {single_stack.is_empty()}")

    # ===============================
    # QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")
    queue = Queue()

    print("\nAdding items to the queue:")
    for value in [10, 20, 30, 40]:
        queue.enqueue(value)
        print(f"Enqueued: {value}")

    print(f"\nFront item using front(): {queue.front()}")

    print("\nRemoving items (FIFO - First In, First Out):")
    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}")

    print("\nTesting dequeue() on an empty queue:")
    print(queue.dequeue())

    print("\nTesting front() on an empty queue:")
    print(queue.front())

    print("\nTesting a single-item queue:")
    single_queue = Queue()
    single_queue.enqueue(100)
    print("Added item: 100")
    print(f"Removed item: {single_queue.dequeue()}")
    print(f"Is the queue empty? {single_queue.is_empty()}")


if __name__ == "__main__":
    main()
