class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def detect(head):
    slow=head
    fast=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:
            return True
    return False

def lenghtofloop(head):
    slow=head
    fast=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:
            lenght=1
            fast=fast.next
            while slow!=fast:
                fast=fast.next
                lenght+=1
            return lenght
    return None
node1=Node(1)
head=node1
node2=Node(2)
node1.next=node2
node3=Node(3)
node2.next=node3
node4=Node(4)
node3.next=node4
node5=Node(5)
node4.next=node5
node5.next=node2
temp=lenghtofloop(head)
if detect(head):
    print(temp)
else:
    print("Cycle not detected")



