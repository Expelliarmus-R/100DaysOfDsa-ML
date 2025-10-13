class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
def reverse(head):
    prev=None
    curr=head
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    return prev
def removemiddle(head):
    slow=head
    fast=head
    prev=None
    while fast and fast.next:
        prev=slow
        slow=slow.next
        fast=fast.next.next
    prev.next=slow.next
    return head
node1=Node(1)
node2=Node(2)
node1.next=node2
node3=Node(3)
node2.next=node3
node4=Node(4)
node3.next=node4
node5=Node(5)
node4.next=node5
head=node1
temp=removemiddle(head)
while temp:
    print(temp.data)
    temp=temp.next
print(None)


