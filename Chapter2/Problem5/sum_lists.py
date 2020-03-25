from Chapter2.linked_list import *


def sum_lists(head1, head2):
    total = 0
    sentinel = LinkedList(0)
    linked_sum = sentinel
    while head1 is not None or head2 is not None:
        if head1 is not None:
            total += head1.data
            head1 = head1.next
        if head2 is not None:
            total += head2.data
            head2 = head2.next
        linked_sum.next = LinkedList(total % 10)
        linked_sum = linked_sum.next
        total //= 10

    if total > 0:
        linked_sum.next = LinkedList(1)
    return sentinel.next
