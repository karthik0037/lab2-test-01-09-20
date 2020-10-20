class Node:
    def __init__(self,data): # Constructor for Node class
        self.data = data
        self.next = None

# Defining the Linked List class
class LinkedList:
    def __init__(self): # Constrctor for LinkedList class
        self.head = None

    # Method to append data
    def append(self,data):
        new_node = Node(data)
        # If head is empty
        if self.head is None:
            self.head = new_node
            return
        # If head is not empty
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    
    # Method to print linked list
    def print_list(self):
        if self.head is None:
            print("EMPTY LINKED LIST")
            return
        cur = self.head
        while cur:
            # Traversing through each element and printing it
            print(cur.data)
            cur = cur.next
    
    # Method to delete the first node
    def del_at_beginning(self):
        self.head = self.head.next
        return


ll = LinkedList() # Creating a linked list
size = int(input("Enter the number of elements you want to add to the Linked List : "))
# Appending data to it
for i in range(size):
    k = input("Enter the data : ")
    ll.append(k)
# Prninting the linked list before deletion
print("The Linked List before deleting the first node : ")
ll.print_list()

# Printing the linked list after deletion
ll.del_at_beginning()
print("The Linked List after deleting the first node : ")
ll.print_list()
