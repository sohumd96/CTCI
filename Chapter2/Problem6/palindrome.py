from Chapter2.linked_list import *


def palindrome(head):
    if head is None or head.next is None:
        return True

    stack = []
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next
    while slow is not None:
        if stack.pop() != slow.data:
            return False
        slow = slow.next
    return True
