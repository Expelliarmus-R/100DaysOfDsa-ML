class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sortList(head):
    if not head or not head.next:
        return head

    zeroHead = Node(-1)
    oneHead = Node(-1)
    twoHead = Node(-1)

    zero = zeroHead
    one = oneHead
    two = twoHead

    temp = head

    while temp:
        if temp.data == 0:
            zero.next = temp
            zero = zero.next
        elif temp.data == 1:
            one.next = temp
            one = one.next
        else:
            two.next = temp
            two = two.next
        temp = temp.next

    zero.next = oneHead.next if oneHead.next else twoHead.next
    one.next = twoHead.next
    two.next = None

    newHead = zeroHead.next

    del zeroHead, oneHead, twoHead

    return newHead


def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# Example
head = Node(1)
head.next = Node(0)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(0)
head.next.next.next.next.next = Node(2)


head = sortList(head)

print("After sorting:")
printList(head)
