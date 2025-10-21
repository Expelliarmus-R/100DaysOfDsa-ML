class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def findmiddle(self, head):
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeTwo(self, l1, l2):
        dummy = Node(-1)
        temp = dummy

        while l1 and l2:
            if l1.data <= l2.data:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
            temp.next = None
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2

        return dummy.next

    def mergeSort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.findmiddle(head)
        right = middle.next
        middle.next = None

        left_sorted = self.mergeSort(head)
        right_sorted = self.mergeSort(right)

        return self.mergeTwo(left_sorted, right_sorted)

    def sort(self):
        self.head = self.mergeSort(self.head)


ll = LinkedList()
ll.head = Node(4)
ll.head.next = Node(2)
ll.head.next.next = Node(1)
ll.head.next.next.next = Node(3)

ll.sort()

temp = ll.head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
