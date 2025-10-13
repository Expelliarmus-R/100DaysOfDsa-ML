from email.quoprimime import header_check


class Node:
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
def removenthfromback(head,pos):
    if not head:
        return None
    reversee = reverse(head)
    temp = reversee
    if pos==1:
        reversee=reversee.next
    else:
        count=1
        while temp and count < pos-1 :
            temp=temp.next
            count+=1
        temp.next=temp.next.next
    head=reverse(reversee)
    return head
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
head = node1

head=removenthfromback(head,1)
temp1=head
while temp1:
    print(temp1.data)
    temp1=temp1.next
print("None")