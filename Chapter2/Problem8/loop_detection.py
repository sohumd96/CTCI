from Chapter2.linked_list import *


def loop_detection(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    if fast is None or fast.next is None:
        return None

    while head != fast:
        head = head.next
        fast = fast.next
    return head
