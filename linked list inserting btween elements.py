print("karthik-121910313037")
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,value):
        if self.head is None:
            new_node  = Node(value)
            self.head=new_node
        else:
            new_node = Node(value)
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node    

    def add_in_btw(self,value,position_value):
        new_node=Node(value)
        temp=self.head
        while temp:
            if temp.data==position_value:
                break
            temp=temp.next
        nxt=temp.next
        temp.next=new_node
        new_node.next=nxt
        
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

d=LinkedList()
N=int(input("enter the number of nodes u want to add to the linkedlist: "))
for i in range(N):
    d.append(input(f'Enter the node data'))
a=input("Enter the value to insert")
b=input("enter after which element you want to add this new value")
d.add_in_btw(a,b)
d.printList() 
