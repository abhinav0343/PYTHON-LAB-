class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_front(self):
        data = int(input("Enter the data of the node: "))
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self):
        data = int(input("Enter the data of the node: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_at_front(self):
        if self.head is None:
            print("List is empty.")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is already empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

def main():
    linked_list = LinkedList()
    linked_list.head = Node(50)
    second = Node(40)
    third = Node(30)
    fourth = Node(20)
    linked_list.head.next = second
    second.next = third
    third.next = fourth
    while True:
        print("\nCurrent Linked List:")
        linked_list.display() 
        print("\nOptions:")
        print("1. Insert at front")
        print("2. Insert at end")
        print("3. Delete at front")
        print("4. Delete at end")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            linked_list.insert_at_front()
        elif choice == 2:
            linked_list.insert_at_end()
        elif choice == 3:
            linked_list.delete_at_front()
        elif choice == 4:
            linked_list.delete_at_end()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
