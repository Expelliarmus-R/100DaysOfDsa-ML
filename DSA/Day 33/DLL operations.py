class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insertatbeg(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode

    def insertatend(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp

    def insertatplace(self,data,pos):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        if pos==1:
            newnode.next=self.head
            self.head=newnode
            return
        temp=self.head
        count=1
        while temp and count < pos-1 :
            temp=temp.next
            count+=1
        newnode.next = temp.next
        temp.next=newnode

    def deletefirst(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head=self.head.next
        self.head.prev=None

    def deletelast(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        if temp.next is None:
            self.head = None
            return
        while temp.next:
            temp=temp.next
        temp.prev.next=None

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")

l1=Linkedlist()
l1.insertatbeg(5)
l1.insertatend(1)
l1.insertatend(1)
l1.insertatplace(2,2)
l1.delbypos(3)
l1.insertatplace(4,4)
# l1.insertatplace(2,2)
# l1.insertatplace(4,1)

l1.display()




