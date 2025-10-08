class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def reverse(head):
    if head==None or head.next==None:
        return head
    new_node=reverse(head.next)
    front=head.next
    front.next=head
    head.next=None
    return new_node
# def print(self):
#     temp=head
#     while temp:
#         print(temp.data,end=" ")
#         temp=temp.next
#     print("None")

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
temp=reverse(head)
while temp:
    print(temp.data,end=" ")
    temp=temp.next
print("None")