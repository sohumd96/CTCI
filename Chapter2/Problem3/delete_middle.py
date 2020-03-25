def delete_middle(head):
    if head.next is not None:
        head.data = head.next.data
        head.next = head.next.next
