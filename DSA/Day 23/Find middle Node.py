class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def middle(head):
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)

middle_node=middle(head)
temp=middle_node
while temp:
    print(temp.data,end="-->")
    temp=temp.next
print("None")