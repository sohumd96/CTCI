from Chapter2.linked_list import *


def intersection(l1, l2):
    i = 0
    j = 0

    dum1 = l1
    dum2 = l2

    while dum1 is not None or dum2 is not None:
        if dum1 is not None:
            i += 1
            dum1 = dum1.next
        if dum2 is not None:
            j += 1
            dum2 = dum2.next

    l3, l4 = (l1, l2) if i > j else (l2, l1)

    for i in range(abs(i - j), 0, -1):
        l3 = l3.next

    while l3 is not None and l4 is not None:
        if l3 == l4:
            return True
        l3 = l3.next
        l4 = l4.next

    return False
