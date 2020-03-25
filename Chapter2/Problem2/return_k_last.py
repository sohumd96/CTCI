def return_k_last(head, k):
    if head is None:
        return None

    slow = head
    fast = head

    for i in range(0, k):
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow.data