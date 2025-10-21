class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.
def reverse(head):
    prev=None
    current=head
    while current :
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    return prev


def addOne(head: Node) -> Node:
    head=reverse(head)
    carry=1
    curr=head
    while curr and carry:
        sum_=curr.data+carry
        curr.data=sum_%10
        carry=sum_//10

        if not curr.next and carry :
            curr.next=Node(carry)
            carry=0
        curr=curr.next
    head=reverse(head)
    return head
