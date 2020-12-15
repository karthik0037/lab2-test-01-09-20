class Node:
    def _init_(self,data): 
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self): 
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    def print_list(self):
        if self.head is None:
            print("EMPTY LINKED LIST")
            return
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def min_max(self):
        if self.head is None:
            print("EMPTY LINKED LIST")
            return (None,None)
        cur = self.head
        mini = None
        maxi = None
        while cur:
            d = cur.data
            if mini==None or d<mini:
                mini = d
            if maxi==None or d>maxi:
                maxi = d
            cur = cur.next
        return (mini,maxi)
        

ll = LinkedList() # Creating a linked list
size = int(input("Enter the number of elements you want to add to the Linked List : "))
# Appending data to it
for i in range(size):
    k = int(input("Enter the data : "))
    ll.append(k)
# Printing the linked list
print("The Linked List: ")
ll.print_list()

# Printing the aximum and minimum of the linked list
minm,maxi = ll.min_max()
print("The minimum element is",minm)
print("The maximum element is",maxi)
