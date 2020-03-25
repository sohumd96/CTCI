from Chapter2.linked_list import *


def partition(l1, part):
    left = LinkedList(0)
    left_temp = left
    right = LinkedList(0)
    right_temp = right

    while l1 is not None:
        if l1.data < part:
            left_temp.next = l1
            left_temp = left_temp.next
        else:
            right_temp.next = l1
            right_temp = right_temp.next
        l1 = l1.next
    right_temp.next = None
    left_temp.next = right.next
    return left.next
