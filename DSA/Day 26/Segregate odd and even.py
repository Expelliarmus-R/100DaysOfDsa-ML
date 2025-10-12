class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
def segregate(head):
    odd=head
    even=head.next
    evenhead=even
    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next=even.next.next
        even=even.next
    odd.next=evenhead
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

temp=segregate(head)
while temp:
    print(temp.data,end="-->")
    temp=temp.next
print("None")
