def remove(head):
    if not head :
        return None
    curr=head
    while curr and curr.next
        next_distinct=curr.next
        while next_distinct and next_distinct.data==curr :
            next_distinct=next_distinct.next
        curr.next=next_distinct
        if next_distinct:
            next_distinct.prev=curr
        curr=curr.next
    return head
