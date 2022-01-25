# A simple Python program for traversal of a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def asda(self):
        max_pages = -1

        h = self.head
        last_pointer = self.head
        temp2 = self.head
        while temp2:
            last_pointer = last_pointer.next
            temp2 = temp2.next.next

        mid_pointer = last_pointer
        prev = None
        while mid_pointer:
            nxt = mid_pointer.next
            mid_pointer.next = prev
            prev = mid_pointer
            mid_pointer = nxt

        while h and prev:
            max_pages = max(max_pages, (h.data + prev.data))
            h = h.next
            prev = prev.next

        print(max_pages)


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(3)
    third = Node(9)
    fourth = Node(4)
    fifth = Node(6)
    sixth = Node(10)

    llist.head.next = second  # Link first node with second
    second.next = third  # Link second node with the third node
    third.next = fourth  # Link second node with the third node
    fourth.next = fifth  # Link second node with the third node
    fifth.next = sixth  # Link second node with the third node

    llist.asda()
