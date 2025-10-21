class solution
    def deletealloccur(head,target):
        if head is None :
            return None
        while head is not None and head.data==target:
            head=head.next
            head.prev=None
        curr=head
        while curr:
            if curr.data==target:
                if curr.next:
                    curr.next.prev=curr.prev
                if curr.prev:
                    curr.prev.next=curr.next
                curr=curr.next
        return head
