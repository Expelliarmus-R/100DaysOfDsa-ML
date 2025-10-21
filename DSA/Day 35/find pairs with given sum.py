def findpair(head,target):
    left=head
    right=head
    while right :
        right=right.next
    found=False
    while left and left.next:
        if right.data+left.data==target:
            found=True
            print(right.data,left.data)
            right=right.prev
            left=left.next
        elif right.data+left.data>target:
            right=right.prev
        else:
            left=left.next
        if not found:
            print("Not found")