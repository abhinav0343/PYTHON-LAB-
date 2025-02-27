class Queue:
    def __init__(self):
        self.queue = []

    def display(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Queue: ", end="")
            for element in self.queue:
                print(element, end=" ")
            print()

    def enqueue(self):
        data = int(input("Enter the data to enqueue: "))
        self.queue.append(data)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty, cannot dequeue.")
        else:
            dequeued_element = self.queue.pop(0)
            print(f"Dequeued: {dequeued_element}")

def main():
    queue = Queue()
    queue.queue.extend([50, 60, 70, 89])
    while True:
        print("\nCurrent Queue:")
        queue.display()
        print("\nOptions:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            queue.enqueue()
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()