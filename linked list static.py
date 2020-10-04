print("karthik-121910313037")
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None


    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
list1=LinkedList()
list1.head=Node(10)
second=Node(20)
third=Node(30)
list1.head.next=second
second.next=third
list1.printList()
