def remove_dups(head):
    if head is None or head.next is None:
        return head
    my_set = set()
    slow = head
    fast = head.next
    while slow is not None:
        my_set.add(slow.data)
        while fast is not None and fast.data in my_set:
            fast = fast.next
        slow.next = fast
        slow = slow.next
    return head


def remove_dups_nobuffer(head):
    if head is None or head.next is None:
        return head
    slow = head
    while slow is not None:
        temp = slow
        fast = temp.next
        while fast is not None:
            while fast is not None and fast.data == slow.data:
                fast = fast.next
            temp.next = fast
            if fast is not None:
                fast = fast.next
            temp = temp.next
        slow = slow.next
    return head
