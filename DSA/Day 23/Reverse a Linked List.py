class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def reverse(head):
    prev=None
    curr=head
    while curr!=None:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    return prev
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
new_head=reverse(head)
temp=new_head

while temp:
    print(temp.data,end="-->")
    temp=temp.next
print("None")

